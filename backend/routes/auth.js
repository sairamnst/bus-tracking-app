const express = require('express');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const router = express.Router();

router.post('/login', (req, res) => {
  const { email, password } = req.body;
  // Replace this with DB lookup
  const user = { email: 'test@test.com', password: bcrypt.hashSync('password', 8) };

  if (email === user.email && bcrypt.compareSync(password, user.password)) {
    const token = jwt.sign({ email: user.email }, 'secret', { expiresIn: '1h' });
    res.json({ success: true, token });
  } else {
    res.status(401).json({ success: false, message: 'Invalid credentials' });
  }
});

module.exports = router;
