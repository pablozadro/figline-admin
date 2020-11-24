const path = require('path');
const { merge } = require('webpack-merge');
const base = require('./config');

module.exports = merge(base, {
  mode: 'development',
  watch: true,
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, '../assets/js'),
    sourceMapFilename: '[name].bundle.js.map'
  },
  devtool: 'source-map'
});
