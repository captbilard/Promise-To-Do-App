const path = require('path');
module.exports = {
    context: path.resolve(__dirname, 'frontend'),
    entry: "/home/bilard/Desktop/Promise-todo-app/Promise-To-Do-App/TODO/frontend/src/index.js",
    watch:true,
    module: {
      rules: [
        {
          test: /\.(js|jsx)$/,
          exclude: /node_modules/,
          use: {
            loader: 'babel-loader'
          }
        }
      ]
    }
};