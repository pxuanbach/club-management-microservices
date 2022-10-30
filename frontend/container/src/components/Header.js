import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => (
  <header>
    <nav>
      <ol className="center-column">
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/club-admin">Club Admin</Link>
        </li>
        <li>
          <Link to="/user-admin">User Admin</Link>
        </li>
      </ol>
    </nav>
  </header>
);

export default Header;