const baseUrl = 'http://localhost:5000/api';

class UserService {
  static async listUsers() {
    try {
      const response = await fetch(`${baseUrl}/v1/users`, {
        headers: {
          'Content-Type': 'application/json'
        },
        method: 'GET',
      });
      const data = await response.json()
      return data
    } catch (err) {
      console.log(err);
      return []
    }
  }

  static async createUser(user_info) {
    try {
      const response = await fetch(`${baseUrl}/v1/users`, {
        headers: {
          'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify(user_info)
      })

      const data = await response.json()
      return data
    } catch (error) {
      console.log(error)
      return null
    }
  }

  static async registerUser(user_info) {
    try {
      const response = await fetch(`${baseUrl}/v1/auth_session/register`, {
        method: 'POST',
        body: JSON.stringify(user_info),
        headers: { 'Content-Type': 'application/json' },
      });

      const data = response.json();
      return data
    } catch (err) {
      console.log(error)
      return null
    }
  }

  static async loginUser(user_info) {
    try {
      const response = await fetch(`${baseUrl}/v1/auth_session/login`, {
        headers: { 'Content-Type': 'application/json' },
        method: 'POST',
        body: JSON.stringify(user_info),
      })

      const data = response.json();
      return data;
    } catch (error) {
      console.log(error)
      return null
    }
  }
}

export default UserService;
