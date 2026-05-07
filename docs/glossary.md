# Glossary

* **FLCE** - Frontend Local Communication Exclusive
* **MI** - Model Information
* **Interlayer** - class to facilitate communication between VRCGA frontend, main VRCGA database and other data (like config files), and VRCGA Service
* **Abstract Interlayer** - abstract class for what methods the interlayer will be required by the model to have implementations for
* **Concrete Interlayer** - an implemented class for an abstract interlayer
* **MSO** - Model Service Outbound (ex. MSOInterlayer), for designating any communication between the frontend and backend/VRCGA service originating from the frontend (ex. frontend querying the database for the dates list, frontend passing login credentials to service)
* **MSI** - Model Service Inbound (ex. MSIInterlayer), for designating any communication between the frontend and backend/VRCGA service originating from the backend/VRCGA service (ex. vrga service sendsing status updates to frontend)
* **VRCGA Service** - The backend service for VRChat Group Assistant
