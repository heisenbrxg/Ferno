/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        ades: {
          green: "#C9F31D",
          darkBg: "#111111",
          cardBg: "#1e1e1e",
          cardBorder: "#2e2e2e",
          textLight: "#a3a3a3"
        }
      },
      animation: {
        'pulse-glow': 'pulse-glow 2s infinite',
      },
      keyframes: {
        'pulse-glow': {
          '0%, 100%': { transform: 'scale(1)', boxShadow: '0 0 0 0 rgba(201, 243, 29, 0.4)' },
          '50%': { transform: 'scale(1.05)', boxShadow: '0 0 0 8px rgba(201, 243, 29, 0)' },
        }
      }
    },
  },
  plugins: [],
}
