const express = require('express');
// var cors = require('cors');
const mysql = require('mysql2');
const { Server } = require('socket.io');
const http = require('http');
const authRoutes = require('./routes/auth');
const busRoutes = require('./routes/bus');

const app = express();
const server = http.createServer(app);
const io = require("socket.io")(httpServer, {
    cors: {
      origin: "http://localhost:3000",
      methods: ["GET", "POST"],
      credentials: true
    }
});


const cors = require('cors');
const corsOptions ={
    origin:'http://localhost:3000', 
    credentials:true,            //access-control-allow-credentials:true
    optionSuccessStatus:200
}
app.use(cors(corsOptions));

app.use(express.json());

app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    next();
  });

// const db = mysql.createConnection({
//   host: 'localhost',
//   user: 'root',
//   password: '',
//   database: 'bus_tracking'
// });

// db.connect(err => {
//   if (err) throw err;
//   console.log('MySQL connected');
// });

app.use('/auth', authRoutes);
app.use('/bus', busRoutes);

let busLocation = { lat: null, lng: null };

io.on('connection', (socket) => {
  console.log('Client connected');

  // Listen for bus location updates from the driver
  socket.on('bus-location-update', (location) => {
    busLocation = location;
    console.log('Bus Location Updated: ', busLocation);

    // Broadcast the bus location to all connected clients (e.g., users)
    io.emit('bus-location-update', busLocation);
  });

  socket.on('disconnect', () => {
    console.log('Client disconnected');
  });
});

server.listen(5000, () => {
  console.log('Server running on port 5000');
});
