import React, { useEffect, useState } from "react";
import { TelemetryInterface } from "../interfaces/telemetry";
import TelemetryContainer from "./telemtryItem";

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

  const getGearNumber = (gearValue: number) => {
    switch (gearValue) {
      case 0:
        return "N";
      case -1:
        return "R";
      default:
        return gearValue;
    }
  };

  return (
    <div className="flex justify-center gap-5 text-white w-full max-w-[1024px]">
      <div className="flex flex-col justify-between">
        <TelemetryContainer className="" title="Fuel">
          <span className="z-0 text-3xl text-center font-mono w-28">{telemetry?.fuel.fuel_level.toFixed(1)}</span>
        </TelemetryContainer>
        <TelemetryContainer className="" title="Oil T">
          <span className="z-0 text-3xl text-center font-mono w-28">{telemetry?.engine.oil_temperature}</span>
        </TelemetryContainer>
        <TelemetryContainer className="" title="Pos">
          <span className="z-0 text-3xl text-center font-mono w-28">{4}</span>
        </TelemetryContainer>
      </div>
      <div className="flex flex-col justify-between">
        <TelemetryContainer className="" title="Speed">
          <span className="z-0 text-3xl text-center font-mono w-28">
            {((telemetry?.vehicle?.speed ?? 0) * 3.6).toFixed(0)}
          </span>
        </TelemetryContainer>
        <TelemetryContainer className="" title="Water T">
          <span className="z-0 text-3xl text-center font-mono w-28">{telemetry?.engine.water_temperature}</span>
        </TelemetryContainer>
        <TelemetryContainer className="" title="Lap">
          <span className="z-0 text-3xl text-center font-mono w-28">{8}</span>
        </TelemetryContainer>
      </div>
      <div className="flex flex-col gap-3">
        <TelemetryContainer className="h-40" title="Gear">
          <span className="z-0 text-8xl text-center font-mono w-28">{getGearNumber(telemetry?.engine?.gear ?? 0)}</span>
        </TelemetryContainer>
        <TelemetryContainer className="" title="RPM">
          <span className="z-0 text-3xl text-center  font-mono w-28">{telemetry?.engine.rpm}</span>
        </TelemetryContainer>
      </div>

      <div className="flex flex-col justify-between gap-3">
        <TelemetryContainer className="" title="Delta Time">
          <span className="z-0 text-3xl text-center  font-mono w-56">{0.59}</span>
        </TelemetryContainer>
        <TelemetryContainer className="" title="Last Lap">
          <span className="z-0 text-3xl text-center font-mono w-56">{"1:39.12"}</span>
        </TelemetryContainer>
        <TelemetryContainer className="" title="Best Lap">
          <span className="z-0 text-3xl text-center font-mono w-56">{"1:38.49"}</span>
        </TelemetryContainer>
      </div>
    </div>
  );
};

export default Telemetry;
