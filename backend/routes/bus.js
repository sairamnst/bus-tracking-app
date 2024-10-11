const express = require('express');
const router = express.Router();

router.get('/location', (req, res) => {
  const busLocations = [
    { id: 1, location: '23.5, 45.6' },
    { id: 2, location: '24.0, 46.0' }
  ];
  res.json(busLocations);
});

module.exports = router;
