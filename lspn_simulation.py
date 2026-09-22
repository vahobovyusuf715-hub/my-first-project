# LSPN - Lunar Solar Power Network
# Simple solar energy simulation

SOLAR_IRRADIANCE = 1361       # W/m², approximate solar irradiance near the Moon
PANEL_AREA = 10               # m²
PANEL_EFFICIENCY = 0.25       # 25%

solar_power = SOLAR_IRRADIANCE * PANEL_AREA * PANEL_EFFICIENCY

print("LSPN Solar Power Simulation")
print("---------------------------")
print(f"Panel area: {PANEL_AREA} m²")
print(f"Panel efficiency: {PANEL_EFFICIENCY * 100:.0f}%")
print(f"Estimated solar power: {solar_power:.1f} W")
print(f"Estimated solar power: {solar_power / 1000:.2f} kW")