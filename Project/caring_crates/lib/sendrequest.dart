import 'package:caring_crates/myprofile.dart';
import 'package:flutter/material.dart';

class SendRequest extends StatefulWidget {
  const SendRequest({Key? key}) : super(key: key);

  @override
  State<SendRequest> createState() => _SendRequestState();
}

class _SendRequestState extends State<SendRequest> {
  
  final TextEditingController _titleController = TextEditingController();
  final TextEditingController _detailsController = TextEditingController();

  void sendRequest() {
    print(_titleController.text);
    print(_detailsController.text);
    // Perform other actions related to sending the request
  }
  String? selectedDonationtype;
  List<String> Donationtype = ['Food', 'pillows', 'Blankets','Education','Medical support']; 

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
          decoration: BoxDecoration(
            color: Colors.transparent,
            borderRadius: BorderRadius.circular(20.0),
          ),
          child: ListView(
            children: [
              const SizedBox(
                height: 50,
              ),
              const Text(
                'Send Request',
                style: TextStyle(fontSize: 25, fontWeight: FontWeight.w600),
              ),
              const SizedBox(
                height: 50,
              ),
              Row(
                children: [
                  const SizedBox(width: 100, child: Text('Donationtype')),
                  Flexible(
                    child: DropdownButton<String>(
                    dropdownColor: Colors.white,
                    value: selectedDonationtype,
                    onChanged: (String? newValue) {
                      setState(() {
                        selectedDonationtype = newValue!;
                      });
                    },
                    isExpanded: true,
                    items: Donationtype.map((String value) {
                      return DropdownMenuItem<String>(
                        value: value,
                        child: Text(value, style: const TextStyle(color: Colors.black),),
                      );
                    }).toList(),
                  ),
                  ),
                ],
              ),
              TextFormField(
                controller: _titleController,
                decoration: InputDecoration(
                  hintText: 'Title',
                ),
              ),
              TextFormField(
                controller: _detailsController,
                decoration: InputDecoration(
                  hintText: ' Details',
                ),
              ),
              const SizedBox(
                height: 50,
              ),
              ElevatedButton(
                onPressed: () {
                  sendRequest();
                },
                child: Text('Send'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
