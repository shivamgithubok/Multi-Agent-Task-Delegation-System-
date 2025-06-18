import axios from 'axios';

// Base URL of your FastAPI backend
const API_BASE = 'http://localhost:8000/api'; // ✅ Change if hosted elsewhere

// 1. Classify user query
export const classifyQuery = (message) =>
  axios.post(`${API_BASE}/classify`, { message });

// 2. Assign agent to a category
export const assignAgent = (category) =>
  axios.post(`${API_BASE}/assign`, { category });

// 3. Retrieve relevant info
export const retrieveInfo = (message) =>
  axios.post(`${API_BASE}/retrieve`, { message });

// 4. Generate final response
export const generateResponse = (data) =>
  axios.post(`${API_BASE}/respond`, data);

// 5. Log interaction to the DB
export const logInteraction = (data) =>
  axios.post(`${API_BASE}/log`, data);