# MRCV1

**Multifunction Radar Combination (MRC) Documentation**

**MRC V1.0 **

Developed by Mikhael da Silva, ... , ...

---
Special thanks to contributors:
Fida 495358
Florent 420571
Diego 102736


---

## **1. Project Overview**

MRC aims to revolutionize IVAO radar operations by combining multiple functionalities into a single platform. With its modular design and user-focused features, MRC enhances air traffic control efficiency and improves virtual aviation experiences.

---

## **2. Planned Features**

### **2.1 Real-Time Radar Tracking**

- Provides an accurate display of aircraft movement within the same network.
- Design based on military radar systems to detect planes within the radar scope.

### **2.2 Mission-Based Training**

- Simulates special mission scenarios for realism in virtual flights.
- Focused on special and military operations.

### **2.3 Identification Friend or Foe (IFF)**

- Simulates air combat training by detecting friendly and unknown aircraft.
- Uses transponder codes and radar interrogation methods.

### **2.4 Multi-Range Scanning**

- Simulates radar systems found on real aircraft.
- Allows users to select scanning modes for enhanced realism.

---

## **3. Layout Overview**

### **Control Buttons**

- **MENU**: Main navigation button; long press to shut down MRC.
- **A-A (Air-to-Air Mode)**: Tracks and monitors airborne targets.
- **A-G (Air-to-Ground Mode)**: Detects and monitors ground-based targets.
- **SNSR (Sensor Management)**: Manages IFF, Bullseye, KML-based mission maps, and radar sources.
- **WPN (Weapon Systems)**: Manages weapons in virtual operational missions.
- **SET**: Execution button for radar modes, IFF settings, and input coordination.
- **R1-R5 & B1-B4**: Multi-function buttons depending on the active mode.

---

## **4. Workflow**

### **4.1 Initial Frame**

- Press MENU to turn on the MRC system.
- A loading screen appears displaying the MRC version.
- Transition to the Main Menu.

### **4.2 Main Menu**

- Functional buttons are located on the left side (MENU, A-A, A-G, SNSR, WPN).
- The bottom buttons (B1-B4) are used for configuration, with B4 dedicated to SETUP.

### **4.3 SET (Settings) Page**

- Configure BULLSEYE NAME, LONGITUDE, and LATITUDE.
- Option to LOAD KML FILE to import mission maps.
- SHOW MAP option to toggle A-A radar visualization.
- Navigation: B2 & B3 (left/right cursor), R1 & R2 (up/down cursor).
- B4 (SET) executes data inputs and toggles settings.

---

## **5. Radar & Sensor Displays**

### **5.1 Air-to-Air (A-A) Radar**

- Displays aircraft positions, bullseye location, and friend/foe status.
- Symbol representation:
  - Green: Friendly aircraft.
  - Yellow: Unknown contact.
  - White: Own aircraft.
- Additional radar information includes bearing, range, and scan settings.

### **5.2 Final Approach Orientation Region (FAOR)**

- Displays a demarcation line from Google Earth for mission training areas.

### **5.3 Interrogator Symbol Interpretation**

- **Red Arc**: Target outside radar angle.
- **Yellow Arc**: No response from the target.
- **Amber Banana Shape**: Incomplete response received.
- **Green Arc**: Complete response received.

### **5.4 IFF Mode Page**

- Mode 1: Military mission codes.
- Mode 2: Unit codes/tail numbers.
- Mode 3/A: ATC-assigned squawk codes.
- Mode 4: Encrypted challenge-response verification.
- Identification is based on VID registration via the SET page.

---

## **6. Weapons & Special Pods**

### **6.1 Weapon Systems**

- Every aircraft is simulated to carry ordnance.
- Air-to-Air Weapons:
  - **IR Missile**: ▲
  - **Semi-Active Missile**: ◯
  - **Active Missile**: □
- Air-to-Ground Weapons:
  - **Free Fall Bomb**: ▲
  - **Laser Guided Bomb (LGB)**: ◯
  - **Joint Direct Action Munition (JDAM)**: □
  - **Anti-Radiation Missile (ARM)**: X
  - **General Air-to-Ground Missile**: ▽
- Weapon management is accessible through the SET menu.

### **6.2 Sensor Pods**

- **Sniper Pod**: Provides electro-optical targeting system for reconnaissance.
- **Electronic Countermeasures (ECM) Pod**: Disrupts enemy radar systems.
- **High-Resolution Targeting System (HTS) Pod**: Simulates tracking of hostile radar systems.

---

## **7. Technical Stack**

### **7.1 Frameworks & Languages**

- **Python** (Main programming language)
- **Panda3D** (Graphics & UI rendering)
- **OpenGL** (Radar visualization & 3D effects)
- **MSFS2020 SimConnect SDK** (Integration with Microsoft Flight Simulator 2020)
- **IVAO API (Whazzup v2)** (Fetching real-time flight data)

### **7.2 Hardware Requirements**

- **Minimum:** Intel i5, 8GB RAM, Dedicated GPU (2GB VRAM)
- **Recommended:** Intel i7, 16GB RAM, RTX 2060 or equivalent GPU

---

## **8. Development Roadmap**

1. **Phase 1: UI & Core Features**

   - Implement basic UI layout.
   - Create functional buttons and menus.
   - Develop radar screen with real-time updates.

2. **Phase 2: Data Integration**

   - Connect to **MSFS2020 via SimConnect**.
   - Fetch live aircraft data from **IVAO API**.

3. **Phase 3: Advanced Features**

   - Implement IFF interrogation logic.
   - Add mission-based training scenarios.
   - Enhance radar scanning capabilities.

4. **Phase 4: Optimization & Testing**

   - Performance improvements.
   - Multiplayer & synchronization testing.

---

---

This document serves as the **foundation for MRC development**, ensuring a structured approach for implementation and future upgrades.

