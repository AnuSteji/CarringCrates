
import 'package:carring_crates/donatenow.dart';
import 'package:carring_crates/myprofile.dart';
import 'package:carring_crates/myrequest.dart';
import 'package:carring_crates/orphanagerequest.dart';
import 'package:carring_crates/sendrequest.dart';
import 'package:flutter/material.dart';
class Dashboard extends StatefulWidget {
  const Dashboard({Key? key}) : super(key: key);

  @override
  State<Dashboard> createState() => _DashboardState();
}

class _DashboardState extends State<Dashboard> {
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
          child: ListView(
            children: [
              Text('carring Crates',style:TextStyle(fontSize: 45,fontWeight:FontWeight.w800),),
              const SizedBox(
                height: 20,
              ),
              Image.asset("assets/orphanage.jpeg"),
              const SizedBox(
                    height: 20,
                  ),
              Text('HELLO,User'),
              const SizedBox(
                height: 20,
              ),
              Column(
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceAround,
                    children: [
                    GestureDetector(
                      onTap: () {
                         Navigator.push(context, MaterialPageRoute(builder: (context) => const DonateNow()));
                  //Navigator.push(context, MaterialPageRoute(builder: (context) => const DonateNow()));
                      },
                      child: Container(
                        color: Colors.cyan,
                        padding: EdgeInsets.all(10),
                        child: Text(
                          'Donate Now',
                          style: TextStyle(
                            fontSize: 20,
                            fontStyle: FontStyle.italic,
                            color: const Color.fromARGB(255, 244, 246, 246),
                            fontWeight: FontWeight.w200,
                          ),
                        ),
                      ),
                    ),


                    GestureDetector(
                      onTap: () {
                        Navigator.push(context, MaterialPageRoute(builder: (context) => const SendRequest()));
                      },
                      child: Container(
                        color: Colors.cyan,
                        padding: EdgeInsets.all(10),
                        child: Text(
                          'Sent Request',
                          style: TextStyle(
                            fontSize: 20,
                            fontStyle: FontStyle.italic,
                            color: const Color.fromARGB(255, 244, 246, 246),
                            fontWeight: FontWeight.w200,
                          ),
                        ),
                      ),
                      ),
                    
                      
                    ],
                  ),
                  const SizedBox(
                    height: 20,
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceAround,
                    children: [
                      GestureDetector(
                      onTap: () {
                        Navigator.push(context, MaterialPageRoute(builder: (context) => const OrphanageRequest()));
                      },
                     child: Container(
                        color: Colors.cyan,
                        padding: EdgeInsets.all(10),
                        child: Text(
                          'Orphanage Request',
                          style: TextStyle(
                            fontSize: 20,
                            fontStyle: FontStyle.italic,color: Colors.white,
                            fontWeight: FontWeight.w200,
                          ),
                        ),
                      ),
                      ),
                       GestureDetector(
                      onTap: () {
                        Navigator.push(context, MaterialPageRoute(builder: (context) => const MyRequest()));
                      },
                      child: Container(
                        color: Colors.cyan,
                        padding: EdgeInsets.all(10),
                        child: Text(
                          'My Request',
                          style: TextStyle(
                            fontSize: 20,
                            fontStyle: FontStyle.italic,
                            color: const Color.fromARGB(255, 244, 248, 248),
                            fontWeight: FontWeight.w200,
                          ),
                        ),
                      ),
                       ),
                      
                    ],
                  ),
                ],
              ),
            ]
            ),
  
        ),
      ),
    );
  }
}