import 'package:carring_crates/myprofile.dart';
import 'package:flutter/material.dart';

class DonateNow
 extends StatefulWidget {
  const DonateNow
  ({super.key});

  @override
  State<DonateNow
  > createState() => _DonatenowState();
}

class  _DonatenowState extends State<DonateNow> {
   final TextEditingController _amountController = TextEditingController(); 
   void editprofile(){
    print(_amountController.text);
   }

@override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        actions: [
          IconButton(
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const MyProfile()),
              );
            },
            icon: Icon(Icons.person), // Replace with the desired icon
          ),
        ],
      ),
       body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Container(
          padding: const EdgeInsets.all(20.0),
          height: 500,
          width: 500,
          decoration: BoxDecoration(
              color: Colors.transparent,
              borderRadius: BorderRadius.circular(20.0)),
              child: ListView( children: [
              Text('Donate Now',style:TextStyle(fontSize: 45,fontWeight:FontWeight.w600),),
              const SizedBox(
                height: 20,
              ),
              TextFormField(
          controller: _amountController,
          decoration: InputDecoration(
          hintText:'Enter Amount'
        ),
        ),
        const SizedBox(
                height: 50,
              ),
        ElevatedButton(onPressed: (){
          DonateNow();
        },child:Text('Donate'))
           ]  
            ),
              ),
              ),
                  );
  }
}

               
  
  