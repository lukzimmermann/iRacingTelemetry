import React, { useEffect, useState } from "react";
import { TelemetryInterface } from "../interfaces/telemetry";

const Telemetry = () => {
  const [telemetry, setTelemetry] = useState<TelemetryInterface>(); // State to store throttle value

  useEffect(() => {
    const eventSource = new EventSource("http://10.0.0.160:8000/telemetry/stream");

    eventSource.onmessage = (event) => {
      try {
        setTelemetry(JSON.parse(event.data));
      } catch (error) {
        console.error("Error parsing telemetry data:", error);
      }
    };

    return () => {
      eventSource.close();
    };
  }, []);

  return (
    <div>
      <h1>Throttle: {telemetry?.engine?.throttle?.toFixed(2) ?? "Loading..."}</h1>
      <h1>Oil Temperature: {telemetry?.engine?.oil_temperature?.toFixed(2) ?? "Loading..."}</h1>
    </div>
  );
};

export default Telemetry;
