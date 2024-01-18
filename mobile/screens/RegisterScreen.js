import { useNavigation } from '@react-navigation/native'
import { useState } from 'react';
import { View, Text, TouchableOpacity, TextInput, StyleSheet } from 'react-native'
import UserService from '../services/userServices';

const RegisterScreen = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const navigation = useNavigation();

  const handleLogin = () => {
    navigation.navigate('Login')
  }

  const handleRegister = async () => {
    try {
      const userData = {
        first_name: firstName,
        lastName: lastName,
        email: email,
        password: password
      }

      const response = await UserService.createUser(userData);
      if (response !== null) navigation.navigate('Login');
      /**
       * Raise Some error notification
       */
    } catch (error) {
      console.log(error)
    }
  }

  return (
    <View style={styles.container}>
      <Text>Register an Account</Text>
      <TextInput placeholder="First Name" style={[styles.loginButton, styles.input]} onChangeText={(v) => setFirstName(v)} value={firstName} />
      <TextInput placeholder="Last Name" style={[styles.loginButton, styles.input]} value={lastName} onChangeText={(v) => setLastName(v)} />
      <TextInput placeholder="Email Address" style={[styles.loginButton, styles.input]} onChangeText={(v) => setEmail(v)} value={email} />
      <TextInput placeholder="Password" style={[styles.loginButton, styles.input]} value={password} onChangeText={(v) => setPassword(v)} secureTextEntry />

      <TouchableOpacity style={styles.loginButton} onPress={handleRegister}>
        <Text style={styles.buttonText}>Register</Text>
      </TouchableOpacity>

      <TouchableOpacity onPress={handleLogin}>
        <Text style={styles.link}>Login to an existing Account</Text>
      </TouchableOpacity>

    </View>
  )
}

const blue = '#0070FF'

const styles = StyleSheet.create({
  title: {
    fontSize: 32,
    fontWeight: 'bold'
  },
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  loginButton: {
    width: '80%',
    height: 50, // Set a fixed height for the button
    justifyContent: "center", // Center the child elements vertically
    alignItems: "center", // Center the child elements horizontally
    padding: 15,
    borderRadius: 5,
    marginTop: 20,
    borderWidth: 1,
    borderColor: blue,
    backgroundColor: blue,
    fontSize: 16,
  },
  input: {
    backgroundColor: 'white',
    borderColor: blue
  },
  buttonText: {
    color: 'white',
    fontSize: 16,
  },
  link: {
    color: blue
  }
})

export default RegisterScreen;
