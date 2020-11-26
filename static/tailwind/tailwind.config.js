module.exports = {
  purge: {
    enabled: false,
    content: ['../index.html']
  },
  theme: {
    flex: {
      '1': '1 1 12%',
      '6': '6 1 76%',
      auto: '1 1 auto',
      initial: '0 1 auto',
      inherit: 'inherit',
      none: 'none',
    },
    fontFamily: {
      display: ['Roboto', 'sans-serif'],
      body: ['Roboto', 'sans-serif'],
    },
    fontSize: {
      'xs': '.75rem',
      'sm': '.8rem',
      'tiny': '.5rem',
      'base': '1rem',
      'lg': '1.25rem',
      'xl': '1.25rem',
      '2xl': '1.5rem',
      '3xl': '1.875rem',
      '4xl': '2.25rem',
      '5xl': '3rem',
      '6xl': '4rem',
      '7xl': '5rem',
    },
    extend: {
      transitionProperty: {
        'gridTemplateColumns': 'span'
      }
    }
  },
  variants: {},
  plugins: [require('tailwindcss'),
    require('autoprefixer'),
  ],
}