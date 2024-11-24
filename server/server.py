from dataclasses import asdict
import irsdk
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import asyncio
import random

from model import Brake, EngineFlags, Environment, Fuel, Lap, Telemetry, Tire, Tires, Vehicle, Engine
ir = irsdk.IRSDK()
ir.startup()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

async def telemetry_stream():
    while True:
        telemetry_data = asdict(parseData(ir))
        yield f"data: {json.dumps(telemetry_data)}\n\n"
        await asyncio.sleep(0.02)

@app.get("/telemetry/stream")
async def telemetry_endpoint():
    return StreamingResponse(telemetry_stream(), media_type="text/event-stream")


def parseData(ir):
    return Telemetry(
        environment=Environment(
            air_density=round(ir["AirDensity"],3), 
            air_pressure=round(ir["AirPressure"],0), 
            air_temperature=round(ir["AirTemp"],1),
            fog_level=round(ir["FogLevel"],1),
            track_temperature=round(ir["TrackTempCrew"],1)), 
        vehicle=Vehicle(
            speed=round(ir["Speed"],3),
            steering_wheel_angle=round(ir["SteeringWheelAngle"],3)),
        engine=Engine(
            rpm=round(ir["RPM"],0), 
            throttle=round(ir["Throttle"],3),
            clutch=round(ir["Clutch"],3),
            gear=ir["Gear"],
            manifold_pressure=round(ir["ManifoldPress"],3),
            oil_level=round(ir["OilLevel"],3),
            oil_pressure=round(ir["OilPress"],3),
            oil_temperature=round(ir["OilTemp"],1),
            voltage=round(ir["Voltage"],3),
            water_level=round(ir["WaterLevel"],3),
            water_temperature=round(ir["WaterTemp"],1),
            engine_flags=EngineFlags(
                water_temperature_warning=bool(ir["EngineWarnings"] & 0x01),
                oil_temperature_warning=bool(ir["EngineWarnings"] & 0x40),
                oil_pressure_warning=bool(ir["EngineWarnings"] & 0x04),
                fuel_pressure_warning=bool(ir["EngineWarnings"] & 0x02),
                engine_stall=bool(ir["EngineWarnings"] & 0x08),
                pit_speed_limiter=bool(ir["EngineWarnings"] & 0x10),
                rev_limiter=bool(ir["EngineWarnings"] & 0x20)
            )),
        fuel=Fuel(
            fuel_level=round(ir["FuelLevel"],3),
            level_pct=round(ir["FuelLevelPct"],3),
            pressure=round(ir["FuelPress"],3),
            use_per_hour=round(ir["FuelUsePerHour"],3)),
        tires=Tires(
            frontLeft=Tire(
                left_carcass_temperature=round(ir["LFtempCL"],1),
                middle_carcass_temperature=round(ir["LFtempCM"],1),
                right_carcass_temperature=round(ir["LFtempCR"],1),
                left_carcass_tread_remaining=round(ir["LFwearL"],3),
                middle_carcass_tread_remaining=round(ir["LFwearM"],3),
                right_carcass_tread_remaining=round(ir["LFwearR"],3)),
            frontRight=Tire(
                left_carcass_temperature=round(ir["LRtempCL"],1),
                middle_carcass_temperature=round(ir["LRtempCM"],1),
                right_carcass_temperature=round(ir["LRtempCR"],1),
                left_carcass_tread_remaining=round(ir["LRwearL"],3),
                middle_carcass_tread_remaining=round(ir["LRwearM"],3),
                right_carcass_tread_remaining=round(ir["LRwearR"],3)),
            rearLeft=Tire(
                left_carcass_temperature=round(ir["RFtempCL"],1),
                middle_carcass_temperature=round(ir["RFtempCM"],1),
                right_carcass_temperature=round(ir["RFtempCR"],1),
                left_carcass_tread_remaining=round(ir["RFwearL"],3),
                middle_carcass_tread_remaining=round(ir["RFwearM"],3),
                right_carcass_tread_remaining=round(ir["RFwearR"],3)),
            rearRight=Tire(
                left_carcass_temperature=round(ir["RRtempCL"],1),
                middle_carcass_temperature=round(ir["RRtempCM"],1),
                right_carcass_temperature=round(ir["RRtempCR"],1),
                left_carcass_tread_remaining=round(ir["RRwearL"],3),
                middle_carcass_tread_remaining=round(ir["RRwearM"],3),
                right_carcass_tread_remaining=round(ir["RRwearR"],3))),
        brake=Brake(
            brake=round(ir["Brake"],3),
            abs_active=ir["BrakeABSactive"]),
        lap=Lap(
            best_lap_time=round(ir["LapLastLapTime"],3),
            last_lap_time=round(ir["LapBestLapTime"],3),
            lap_count=round(ir["LapCompleted"],3),
            position=round(ir["PlayerCarPosition"],3),
            delta_time=round(ir["LapDeltaToBestLap"],3)
        )
    )