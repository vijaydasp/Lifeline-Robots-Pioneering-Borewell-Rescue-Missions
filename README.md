# Lifeline Robots: Pioneering Borewell Rescue Missions

## 🚀 Project Overview

The **Borewell Rescue Robot** is designed to **safely and efficiently rescue children trapped in borewells**, automating and accelerating a process that has traditionally been time-consuming, dangerous, and resource-intensive.

By leveraging **Raspberry Pi, a pick-and-place robotic arm, and live sensor data streaming**, the system allows remote monitoring and control, minimizing risk while maximizing rescue speed.

---

## 📌 Abstract

Incidents of children falling into borewells have increased, and conventional rescue methods are slow and risky. This system provides:

* A **pick-and-place robotic arm** to safely retrieve victims.
* **Raspberry Pi-based live video streaming** for position assessment.
* Real-time monitoring of **temperature, humidity, and distance**.
* **Web or app-based remote control** for safe operation.

The design minimizes rescue time and human risk while improving success rates.

---

## 🪐 Features

✅ **Real-time environmental monitoring** using sensors.
✅ **Pick-and-place rescue mechanism** with servo motor control.
✅ **Pi Camera integration for live streaming.**
✅ **Gas detection for borewell environment safety.**
✅ **Remote control and monitoring via webpage or app.**
✅ **Compact and portable chassis design.**

---

## 🖼️ Block Diagram

<img width="857" height="473" alt="image" src="https://github.com/user-attachments/assets/d9bbfdf4-baa8-49eb-9759-541c083f40af" />

<img width="880" height="583" alt="image" src="https://github.com/user-attachments/assets/0b270c34-89b4-407b-b477-42c8fc45e602" />



---

## ⚙️ Hardware Used

* Raspberry Pi 4 Model B
* Pi Camera
* Servo Motor & DC Motor with L293D Motor Driver
* DHT11 Temperature and Humidity Sensor
* MQ6 Gas Sensor
* Ultrasonic Sensor
* Power Supply Module with transformer, rectifier, and voltage regulator
* LEDs, resistors, and chassis for assembly

---

## 🛠️ Software and Libraries

* Python with `RPi.GPIO`, `picamera`, `Adafruit-DHT`, and other sensor libraries
* DIPTRACE for PCB design
* WOKWI and CIRCUITO.IO for simulation
* Flutter-based Android/iOS app for control and monitoring

---

## 📈 Methodology

1. **Power Management:** AC stepped down and regulated to 5V DC.
2. **Sensor Integration:** DHT11, MQ6, and ultrasonic sensor connected to Raspberry Pi for real-time data.
3. **Camera Integration:** Pi Camera connected for live video feed.
4. **Motor Control:** Servo and DC motors managed using L293D via GPIO.
5. **Remote Monitoring:** Data and video streamed to a web/app interface for live control.

---

## ✅ Results

* Successfully developed and tested a **compact rescue robot**.
* Demonstrated **live monitoring and control** using the Flutter app.
* Validated sensor accuracy and reliability in test environments.
* Proved the system’s ability to reduce manual labor and rescue time.

---

## ⚖️ Advantages

✔️ **Non-invasive rescue**, no need to dig parallel pits.
✔️ **Faster response and safer operation**.
✔️ **Sensor-based monitoring** for situational awareness.
✔️ **Manual control capability for precise rescue.**

## ⚠️ Limitations

⚠️ Limited depth/diameter operation based on borewell constraints.
⚠️ Potential risk of damage to borewell walls during operation.
⚠️ Dependence on power supply reliability.

---

## 🏁 Conclusion

The **Borewell Rescue Robot** offers a **breakthrough in automating child rescue missions**, providing a **safe, efficient, and reliable system** for high-risk scenarios. Future improvements can integrate:

* **AI for object detection and path planning.**
* **Autonomous navigation and gripping.**
* **Enhanced environmental sensing for complex conditions.**

This system represents a significant step towards **leveraging robotics for social good and disaster response.**

---

## 🎥 Demo

<img width="624" height="660" alt="image" src="https://github.com/user-attachments/assets/ad26b11f-a005-445b-9334-afd62fbafe6d" />

<img width="350" height="600" alt="image" src="https://github.com/user-attachments/assets/bbf986b8-fc42-411b-80a5-573f0d091279" />

<img width="809" height="598" alt="image" src="https://github.com/user-attachments/assets/4b854275-2d0d-4ad1-8c1c-14dd96d1d1e6" />

<img width="608" height="953" alt="image" src="https://github.com/user-attachments/assets/c128dfb1-dbf7-46ff-b837-88806678bc23" />



---

## 🤝 Contributing

Pull requests and suggestions are welcome to improve and extend this life-saving project.

---

## 📧 Contact

For questions or collaboration:

**Vijay Das**

Email - vijaydasd2@gmail.com

LinkedIn - https://www.linkedin.com/in/vijay-das-p-a42068283?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BxyyRRfIGRJ%2BYk8u1yhtC9g%3D%3D

---
