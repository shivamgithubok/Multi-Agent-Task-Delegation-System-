import React, { useState } from 'react';
import {
  classifyQuery,
  assignAgent,
  retrieveInfo,
  generateResponse,
  logInteraction
} from '../services/api';

const TicketForm = ({ onResult }) => {
  const [query, setQuery] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      // 1. Classify
      const { data: classifyData } = await classifyQuery(query);
      const category = classifyData.category;

      // 2. Assign agent
      const { data: assignData } = await assignAgent(category);
      const assigned_agent = assignData.assigned_agent;

      // 3. Retrieve info
      const { data: retrieveData } = await retrieveInfo(query);
      const retrieved_info = retrieveData.retrieved_answer;

      // 4. Generate final response
      const { data: responseData } = await generateResponse({
        original_query: query,
        category,
        assigned_agent,
        retrieved_info
      });

      const final_response = responseData.response;

      // 5. Log interaction
      await logInteraction({
        user_query: query,
        category,
        assigned_agent,
        retrieved_info,
        final_response
      });

      onResult({
        query,
        category,
        assigned_agent,
        retrieved_info,
        final_response
      });

    } catch (error) {
      console.error('Error handling ticket:', error);
      alert('Something went wrong.');
    } finally {
      setLoading(false);
      setQuery('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="p-4 shadow-lg bg-white rounded-lg">
      <label className="block mb-2 text-gray-700 font-bold">Enter your query:</label>
      <textarea
        className="w-full border rounded p-2 mb-4"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        required
        rows={4}
      />
      <button
        type="submit"
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        disabled={loading}
      >
        {loading ? 'Processing...' : 'Submit'}
      </button>
    </form>
  );
};

export default TicketForm;
