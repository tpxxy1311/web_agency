// Improved JSX code
import React from 'react';
import Link from 'next/link';

const Header = () => {
  return (
    <header className="header">
      <nav className="nav" aria-label="Main Navigation">
        <Link href="/" className="nav-logo">
          Your Logo
        </Link>
        <ul className="nav-list">
          <li className="nav-item">
            <Link href="/" className="nav-link">Home</Link>
          </li>
          {/* Add more navigation links as needed */}
        </ul>
      </nav>
    </header>
  );
};

export default Header;
