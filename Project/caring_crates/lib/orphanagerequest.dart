import 'package:caring_crates/myprofile.dart';
import 'package:flutter/material.dart';

class OrphanageRequest extends StatefulWidget {
  const OrphanageRequest({super.key});

  @override
  State<OrphanageRequest> createState() => _OrphanageRequestState();
}

class _OrphanageRequestState extends State<OrphanageRequest> {
  @override
  Widget build(BuildContext context) {
   return Scaffold(
      appBar: AppBar(
        actions: [
          IconButton(
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => const MyProfile(),
                ),
              );
            },
            icon: Icon(Icons.person),
          )
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(5.0),
        child: Column(
          children: [
            Center(child: Text('Orphanage Request',style: TextStyle(fontSize: 30,fontStyle: FontStyle.italic,fontWeight: FontWeight.bold,),)),
            const SizedBox(
                    height: 50,
                  ),
            Container(
              padding: const EdgeInsets.all(20.0),
              width: 280,
              decoration: BoxDecoration(
                 color: Colors.lime,
                borderRadius: BorderRadius.circular(20.0),
              ),
              
              child: Column(
                children: [
                  
                  Text('Orphanage Name'),
                  const SizedBox(
                    width: 20,
                  ),
                      Text('Donation Type'),
                      const SizedBox(
                        width: 20,
                      ),
                      Text('Date'),
                ],
              ),
            ),
            const SizedBox(
                    height: 20,
                  ),
            Container(
              padding: const EdgeInsets.all(20.0),
              width: 280,
              decoration: BoxDecoration(
                  color: Colors.lime,
                borderRadius: BorderRadius.circular(20.0),
              ),
              child: Column(
                children: [
                  
                  Text('Orphanage Name'),
                  const SizedBox(
                    width: 20,
                  ),
                      Text('Donation Type'),
                      const SizedBox(
                        width: 20,
                      ),
                      Text('Date'),
                ],
              ),
            ),
            const SizedBox(
                    height: 20,
                  ),
          Container(
              padding: const EdgeInsets.all(20.0),
              width: 280,
              decoration: BoxDecoration(
                  color: Colors.lime,
                borderRadius: BorderRadius.circular(20.0),
              ),
              child: Column(
                children: [
                  
                  Text('Orphanage Name'),
                  const SizedBox(
                    width: 20,
                  ),
                      Text('Donation Type'),
                      const SizedBox(
                        width: 20,
                      ),
                      Text('Date'),
                ],
                  ),
            ),
          ],
        ),
      ),
    );
  }
}