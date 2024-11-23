from dataclasses import asdict
import irsdk
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import json
import asyncio
import random

from model import Brake, Enviroment, Fuel, Telemetry, Tire, Tires, Vehicle, Engine
ir = irsdk.IRSDK()
ir.startup()

app = FastAPI()

async def telemetry_stream():
    while True:
        # Simulierte Telemetriedaten
        telemetry_data = json.dumps(asdict(parseData(ir)), indent=4)
        # Streamen der Daten im SSE-Format
        yield f"data: {json.dumps(telemetry_data)}\n\n"
        await asyncio.sleep(0.05)  # 10 Hz Update-Rate

@app.get("/telemetry/stream")
async def telemetry_endpoint():
    return StreamingResponse(telemetry_stream(), media_type="text/event-stream")


def parseData(ir):
    return Telemetry(
        enviroment=Enviroment(
            air_density=round(ir["AirDensity"],3), 
            air_pressure=round(ir["AirPressure"],0), 
            air_temperatur=round(ir["AirTemp"],1),
            fog_level=round(ir["FogLevel"],1),
            track_temperature=round(ir["TrackTempCrew"],1)), 
        vehicle=Vehicle(
            speed=round(ir["Speed"],3),
            steering_wheel_abgle=round(ir["SteeringWheelAngle"],3)),
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
            water_temperature=round(ir["WaterTemp"],1)),
        fuel=Fuel(
            fuel_level=round(ir["FuelLevel"],3),
            level_pct=round(ir["FuelLevelPct"],3),
            pressure=round(ir["FuelPress"],3),
            use_per_houre=round(ir["FuelUsePerHour"],3)),
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
            abs_active=ir["BrakeABSactive"])
    )