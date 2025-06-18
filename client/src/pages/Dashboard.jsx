import React, { useState } from 'react';
import TicketForm from '../components/TicketForm';

const Dashboard = () => {
  const [result, setResult] = useState(null);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-2xl font-bold mb-6 text-center">AI Support Assistant</h1>
      <div className="max-w-3xl mx-auto">
        <TicketForm onResult={setResult} />
        {result && (
          <div className="mt-6 p-4 bg-white shadow-md rounded-lg">
            <h2 className="text-xl font-semibold mb-2 text-green-700">AI Response</h2>
            <p className="mb-2"><strong>Final Response:</strong> {result.final_response}</p>
            <p className="text-sm text-gray-500">[Category: {result.category}, Assigned: {result.assigned_agent}]</p>
            <details className="mt-2 text-sm text-gray-600">
              <summary className="cursor-pointer">See Details</summary>
              <pre className="mt-2 whitespace-pre-wrap">{JSON.stringify(result, null, 2)}</pre>
            </details>
          </div>
        )}
      </div>
    </div>
  );
};

export default Dashboard;
