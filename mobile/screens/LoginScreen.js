import React, { useEffect, useState } from "react";
import { Text, View, StyleSheet, TouchableOpacity, TextInput } from "react-native";
import UserService from "../services/userServices";
import { useNavigation } from "@react-navigation/native";

const LoginScreen = () => {
  const [users, setUsers] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigation = useNavigation();

  useEffect(() => {
    const fetchData = async () => {
      const data = await UserService.listUsers();
      console.log(data)
    }

    fetchData();
  }, [])

  const handleLogin = () => {
    console.log(email, password);
    navigation.navigate('Home')
  };

  const handleRegistration = () => {
    navigation.navigate('Register');
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Sacco Management</Text>
      <Text>Log in to your Account</Text>
      <TextInput placeholder="email address" style={[styles.loginButton, styles.input]} onChangeText={(v) => setEmail(v)} value={email} />
      <TextInput placeholder="password" style={[styles.loginButton, styles.input]} value={password} onChangeText={(v) => setPassword(v)} secureTextEntry />
      <TouchableOpacity style={styles.loginButton} onPress={handleLogin}>
        <Text style={styles.buttonText}>Login</Text>
      </TouchableOpacity>

      <TouchableOpacity onPress={handleRegistration}>
        <Text style={styles.link}>Register an account</Text>
      </TouchableOpacity>
    </View>
  );
};

export default LoginScreen;

const blue = "#007AFF";

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
});
