class Sessions {
  static set(key, value) {
    sessionStorage.setItem(key, value);
  }

  static get(key) {
    sessionStorage.getItem(key);
  }
}

export default Sessions;
