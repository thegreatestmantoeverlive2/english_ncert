
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders chapters link', () => {
  render(<App />);
  const linkElement = screen.getByText(/Chapters/i);
  expect(linkElement).toBeInTheDocument();
});
