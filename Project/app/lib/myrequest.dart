import 'package:carring_crates/myprofile.dart';
import 'package:flutter/material.dart';

class MyRequest extends StatefulWidget {
  const MyRequest({super.key});

  @override
  State<MyRequest> createState() => _MyRequestState();
}

class _MyRequestState extends State<MyRequest> {
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
          ),
          const SizedBox(
                    height: 80,
                  ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(5.0),
        child: Column(
          children: [
            Center(
              child: Container(
                padding: const EdgeInsets.all(20.0),
                width: 280,
                decoration: BoxDecoration(
                 color: Colors.lime,
                  borderRadius: BorderRadius.circular(20.0),
                ),
                
                child: Column(
                  children: [
                    
                    Text('Title'),
                    const SizedBox(
                      width: 20,
                    ),
                        Text('Type'),
                        const SizedBox(
                          width: 20,
                        ),
                        Text('Details'),
                        const SizedBox(
                          width: 20,
                        ),
                        Text('Orphanage'),
                  ],
                ),
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
                  
                  Text('Title'),
                  const SizedBox(
                    width: 20,
                  ),
                      Text('Type'),
                      const SizedBox(
                        width: 20,
                      ),
                      Text('Details'),
                      const SizedBox(
                        width: 20,
                      ),
                      Text('Orphanage'),
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
                  
                  Text('Title'),
                  const SizedBox(
                    width: 20,
                  ),
                      Text('Type'),
                      const SizedBox(
                        width: 20,
                      ),
                      Text('Details'),
                      const SizedBox(
                        width: 20,
                      ),
                      Text('Orphanage'),
                ],
                  ),
            ),
          ],
        ),
      ),
    );
  }
}