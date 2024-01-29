import 'package:caring_crates/dashboard.dart';
import 'package:caring_crates/forgot_password.dart';
import 'package:caring_crates/registration.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';

class Login extends StatefulWidget {
  const Login({super.key});

  @override
  State<Login> createState() => LoginState();
}

class LoginState extends State<Login> {
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
   
   
  Future<void> Login() async {
    
    print(_emailController.text);
    print(_passwordController.text);
    // gotoDashboard();
    try {
        final FirebaseAuth auth = FirebaseAuth.instance;
        final UserCredential userCredential =
            await auth.signInWithEmailAndPassword(
          email: _emailController.text.trim(),
          password: _passwordController.text.trim(),
        );
        Navigator.push(context, MaterialPageRoute(builder: (context) => const Dashboard()));
      } catch (e) {
        // Handle login failure and show an error toast.
        String errorMessage = 'Login failed';

        if (e is FirebaseAuthException) {
          errorMessage = e.code;
        }

        Fluttertoast.showToast(
          msg: errorMessage,
          toastLength: Toast.LENGTH_SHORT,
          gravity: ToastGravity.BOTTOM,
          backgroundColor: Colors.red,
          textColor: Colors.white,
        );
      }
  }
  @override
  Widget build(BuildContext context) {
    return  Scaffold(
        body: Padding(
          padding: const EdgeInsets.all(20.0),
          child:ListView(
            children: [
              SizedBox(
                height: 80,
              ),
              Text('Login',style: TextStyle(fontSize: 25.0,fontStyle: FontStyle.italic),),
              SizedBox(
                height: 30,
              ),
              TextFormField(
                controller: _emailController,
                decoration: InputDecoration(
                  hintText: 'Enter Email'
                ),
              ),
              SizedBox(
                height: 30,
              ),
               TextFormField(
                obscureText: true,
                controller: _passwordController,
                decoration: InputDecoration(
                  hintText: 'Enter Password'
                ),
              ),
              SizedBox(
                height: 10,
              ),
              GestureDetector(
                onTap: (){
                 Navigator.push(context, MaterialPageRoute(builder: (context) => const ForgotPassword())); 
                },
              child: const Text('Forgot Password ',style:TextStyle(fontSize: 10.0 ))),
              const SizedBox(
                height: 30,
              ),
              ElevatedButton(onPressed: (){
                Login();
              }, child: Text('Login')),
              SizedBox(
                height: 10,
              ),
              GestureDetector(
                onTap: (){
                 Navigator.push(context, MaterialPageRoute(builder: (context) => const Registration())); 
                },
                child: const Text('Create an account',style:TextStyle(fontSize: 10.0 ),))
              
            ],
          )    
        ),
      );
  }
  
  // void gotoDashboard(){
  //       Navigator.push(context, MaterialPageRoute(builder: (context) => const Dashboard(),));
  //   }
  }