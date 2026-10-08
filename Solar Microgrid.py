## Solar Microgrid 

This program simulates a **solar microgrid** by checking solar power generation, load demand, and battery status.

```
# Solar Microgrid Monitoring

solar_power = float(input("Enter Solar Power Generated (kW): "))
load_power = float(input("Enter Load Demand (kW): "))
battery = float(input("Enter Battery Level (%): "))

print("\n--- Solar Microgrid Status ---")
print("Solar Power =", solar_power, "kW")
print("Load Demand =", load_power, "kW")
print("Battery Level =", battery, "%")

if solar_power >= load_power:
    extra_power = solar_power - load_power
    print("Load supplied by Solar Power")
    print("Extra Power =", extra_power, "kW")

    if battery < 100:
        print("Battery: CHARGING")

elif battery > 20:
    shortage = load_power - solar_power
    print("Solar power is insufficient")
    print("Power Shortage =", shortage, "kW")
    print("Battery: SUPPLYING POWER")

else:
    print("WARNING: Low Solar Power and Low Battery!")
    print("Backup Supply: REQUIRED")
```

### Example Output

```
Enter Solar Power Generated (kW): 10
Enter Load Demand (kW): 7
Enter Battery Level (%): 60

--- Solar Microgrid Status ---
Solar Power = 10.0 kW
Load Demand = 7.0 kW
Battery Level = 60.0 %
Load supplied by Solar Power
Extra Power = 3.0 kW
Battery: CHARGING
```

### Simple Concept

```
Solar Panels → Load
      ↓
   Battery
      ↓
 Backup Supply
```

- **Solar power \> Load:** Extra power charges the battery.
- **Solar power \< Load:** Battery supplies the shortage.
- **Solar + Battery insufficient:** Backup supply is required.

**Project name:** Solar Microgrid Monitoring and Energy Management System

**Main concepts:** Solar generation, load demand, battery storage, energy management, and backup power.
