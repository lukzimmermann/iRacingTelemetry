from dataclasses import dataclass


@dataclass
class Vehicle:
    speed: float
    steering_wheel_abgle: float
    
@dataclass
class Engine:
    rpm: int
    throttle: float
    clutch: float
    gear: int
    manifold_pressure: float
    oil_level: float
    oil_pressure: float
    oil_temperature: float
    voltage: float
    water_level: float
    water_temperature: float

@dataclass
class Fuel:
    fuel_level: float
    level_pct: int
    pressure: float
    use_per_houre: float


@dataclass
class Tire:
    left_carcass_temperature: float
    middle_carcass_temperature: float
    right_carcass_temperature: float
    left_carcass_tread_remaining: float
    middle_carcass_tread_remaining: float
    right_carcass_tread_remaining: float


@dataclass
class Tires:
    frontLeft: Tire
    frontRight: Tire
    rearLeft: Tire
    rearRight: Tire

@dataclass
class Brake:
    brake: float
    abs_active: bool

@dataclass
class Enviroment:
    air_density: float
    air_pressure: float
    air_temperatur: float
    fog_level: float
    track_temperature: float

@dataclass
class Telemetry:
    enviroment: Enviroment
    vehicle: Vehicle
    engine: Engine
    fuel: Fuel
    tires: Tires
    brake: Brake
