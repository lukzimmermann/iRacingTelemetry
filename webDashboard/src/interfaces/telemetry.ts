export interface Vehicle {
  speed: number;
  steering_wheel_angle: number;
}

export interface Engine {
  rpm: number;
  throttle: number;
  clutch: number;
  gear: number;
  manifold_pressure: number;
  oil_level: number;
  oil_pressure: number;
  oil_temperature: number;
  voltage: number;
  water_level: number;
  water_temperature: number;
}

export interface Fuel {
  fuel_level: number;
  level_pct: number;
  pressure: number;
  use_per_hour: number;
}

export interface Tire {
  left_carcass_temperature: number;
  middle_carcass_temperature: number;
  right_carcass_temperature: number;
  left_carcass_tread_remaining: number;
  middle_carcass_tread_remaining: number;
  right_carcass_tread_remaining: number;
}

export interface Tires {
  frontLeft: Tire;
  frontRight: Tire;
  rearLeft: Tire;
  rearRight: Tire;
}

export interface Brake {
  brake: number;
  abs_active: boolean;
}

export interface Environment {
  air_density: number;
  air_pressure: number;
  air_temperature: number;
  fog_level: number;
  track_temperature: number;
}

export interface TelemetryInterface {
  environment: Environment;
  vehicle: Vehicle;
  engine: Engine;
  fuel: Fuel;
  tires: Tires;
  brake: Brake;
}
