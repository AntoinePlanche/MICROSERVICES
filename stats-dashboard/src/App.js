import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [weatherData, setWeatherData] = useState(null);
  const [newsData, setNewsData] = useState(null);
  const [randomStatsData, setRandomStatsData] = useState(null);

  const fetchWeatherData = async () => {
    const response = await axios.get('http://127.0.0.1/weather/Montreal');
    setWeatherData(response.data);
  };

  const fetchNewsData = async () => {
    const response = await axios.get('http://127.0.0.1/news');
    setNewsData(response.data);
  };

  const fetchRandomStatsData = async () => {
    const response = await axios.get('http://127.0.0.1/stats');
    setRandomStatsData(response.data);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Dashboard de Statistiques</h1>
      </header>
      <div className="App-buttons">
        <button className="button" id="weather-btn" onClick={fetchWeatherData}>Climat</button>
        <button className="button" id="news-btn" onClick={fetchNewsData}>Actualités</button>
        <button className="button" id="stats-btn" onClick={fetchRandomStatsData}>Statistiques Aléatoires</button>
      </div>
      <div className="App-content">
        <div className="column">
          <h2>Climat</h2>
          <div className="data-box">{weatherData && <p>{JSON.stringify(weatherData, null, 2)}</p>}</div>
        </div>
        <div className="column">
          <h2>Actualités</h2>
          <div className="data-box">{newsData && <p>{JSON.stringify(newsData, null, 2)}</p>}</div>
        </div>
        <div className="column">
          <h2>Statistiques</h2>
          <div className="data-box">{randomStatsData && <p>{JSON.stringify(randomStatsData, null, 2)}</p>}</div>
        </div>
      </div>
    </div>
  );
}

export default App;
