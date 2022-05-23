import { useState } from 'react';
import './App.css';

function App() {

  const [form, setForm] = useState({
    title: '',
    body: '',
  });

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log("submit");
    let response = await fetch(`/sentiment/${form.body}`, { method: 'POST' });
    const data = await response.json();
    console.log(data)
  }
  // TODO: Add a submit handler to the form
  // Post form data to the server, responding with the details of the new post + the sentiment score
  return (
    <div className="App">
      <h2>Neat Journal app</h2>
      <form onSubmit={handleSubmit}>
        <input onChange={handleChange} value={form.title} type='text' name='title' />
        <textarea onChange={handleChange} value={form.body} name='body'></textarea>
        <input type='submit' />
      </form>
    </div>
  );
}

export default App;
