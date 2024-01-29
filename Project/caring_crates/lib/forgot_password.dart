import 'package:flutter/material.dart';

class ForgotPassword extends StatefulWidget {
  const ForgotPassword({super.key});

  @override
  State<ForgotPassword> createState() => _ForgotPasswordState();
}

class _ForgotPasswordState extends State<ForgotPassword> {
  final TextEditingController _emailController = TextEditingController(); 
  void ForgotPassword(){
    print(_emailController.text);
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
    body:Padding(
    padding:const EdgeInsets.all(20.0),
    child:Column(
      children:[
        SizedBox(
                height: 80,
              ),
        Text('Forgot Password',style: TextStyle(fontSize: 25.0,fontStyle: FontStyle.italic),),
        SizedBox(
                height: 50,
              ),
        TextFormField(
          controller: _emailController,
          decoration: InputDecoration(
          hintText:'Enter Your Email'
        ),
        ),
        ElevatedButton(onPressed: (){
          ForgotPassword();
        },child:Text('Send Link'))
      ],
    ),
    ),
    );
  }
}