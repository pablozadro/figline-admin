const path = require('path');

module.exports = {
  entry: {
    'core': path.resolve(__dirname, '../src/js/index.js')
  },
  module: {
    rules: [
      { 
        test: /\.js$/, 
        exclude: /node_modules/, 
        loader: 'babel-loader'
      }      
    ]
  },
  resolve: {
    alias: {
			'@': path.resolve(__dirname, '../src/js')
    },
    extensions: [ '.js']
	}  
};
