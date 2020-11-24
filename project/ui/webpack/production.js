const path = require('path');
const { merge } = require('webpack-merge');
const base = require('./config');

module.exports = merge(base, {
  mode: 'production',
  watch: false,
  output: {
    filename: '[name].bundle.min.js',
    path: path.resolve(__dirname, '../assets/js'),
    sourceMapFilename: '[name].bundle.min.js.map'
  },
  devtool: 'source-map'
});
