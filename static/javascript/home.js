window.addEventListener('DOMContentLoaded', () => {
  const searchBox = document.querySelector('.search-box');
  const keywords = [
    "python",
    "react.js",
    "javascript",
    "django",
    "html",
    "css",
    "flask",
    "c",
    "c++",
    "c#",
    "aws",
    "node.js",
    "mysql",
    "postgresql",
    "ruby on rails",
    "java",
    "go",
    "kotlin",
    "angular",
    "svelte",
    "nosql",
    "typescript",
    "vue.js",
    "graphql",
    "mongodb",
    "react-native",
    "flutter",
    "r",
    "deep learning",
    "sass",
    "php",
    "ruby",
    "docker",
    "mobx",
    "redux",
  ]

  const getRandomKeyword = () => keywords[parseInt(Math.random() * keywords.length)];

  const iterateKeywords = () => {
    let previousKeyword = ""
    return setInterval(() => {
      let keyword = ""
      do {
        keyword = getRandomKeyword();
      } while (previousKeyword === keyword);
      previousKeyword = keyword;
      searchBox.setAttribute("placeholder", keyword);
    }, 1000);
  }

  let interval = iterateKeywords();
  let value = ""
  searchBox.addEventListener('focus', () => {
    searchBox.value = value;
    searchBox.setAttribute("placeholder", "");
    clearInterval(interval);
  });

  searchBox.addEventListener('blur', () => {
    value = searchBox.value;
    searchBox.value = "";
    searchBox.setAttribute("placeholder", getRandomKeyword());
    interval = iterateKeywords();
  });

  window.addEventListener('unload', () => {
    clearInterval(interval);
  })
})