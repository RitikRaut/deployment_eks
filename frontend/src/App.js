import React, { useState, useEffect } from 'react';

function App() {
  const [pods, setPods] = useState([]);

  useEffect(() => {
    fetch('/pods')
      .then((res) => res.json())
      .then((data) => setPods(data));
  }, []);

  return (
    <div>
      <h1>Pod and Node Details</h1>
      <ul>
        {pods.map((pod, index) => (
          <li key={index}>
            <p>Pod Name: {pod.pod_name}</p>
            <p>Pod IP: {pod.pod_ip}</p>
            <p>Node Name: {pod.node_name}</p>
            <p>Node IP: {pod.node_ip}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
