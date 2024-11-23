import React, { useState, useEffect } from "react";

const Telemetry = () => {
  const [telemetry, setTelemetry] = useState<any>(null);

  useEffect(() => {
    // Connect to the WebSocket server
    const socket = new WebSocket("ws://10.0.0.160:8000/telemetry/stream");

    socket.onopen = () => {
      console.log("WebSocket connection established");
    };

    socket.onmessage = (event) => {
      // Parse the received JSON data
      const data = JSON.parse(event.data);
      setTelemetry(data);
    };

    socket.onerror = (error) => {
      console.error("WebSocket error:", error);
    };

    socket.onclose = () => {
      console.log("WebSocket connection closed");
    };

    // Cleanup on component unmount
    return () => {
      socket.close();
    };
  }, []); // Run only once when the component mounts

  return (
    <div>
      <h1>Telemetry Data</h1>
      {telemetry ? (
        <ul>
          <li>Speed: {telemetry.vehicle.speed}</li>
          <li>Throttle: {telemetry.engine.throttle}</li>
          <li>Gear: {telemetry.engine.gear}</li>
        </ul>
      ) : (
        <p>Waiting for telemetry data...</p>
      )}
    </div>
  );
};

export default Telemetry;
