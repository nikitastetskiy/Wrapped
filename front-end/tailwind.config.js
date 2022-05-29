// tailwind.config.js
module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      "colors": {
        "brand": {
          "50": "#F9FBFA",
          "100": "#F1F4F3",
          "200": "#E2E9E7",
          "300": "#D1DCD9",
          "400": "#BFCECB",
          "500": "#ABBFBA",
          "600": "#ABBFBA",
          "700": "#ABBFBA",
          "800": "#ABBFBA",
          "900": "#ABBFBA"
        },
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}