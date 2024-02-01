import 'package:flutter/material.dart';
import 'dart:io';
import 'package:image_picker/image_picker.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class Registration extends StatefulWidget {
  const Registration({Key? key});

  @override
  State<Registration> createState() => RegistrationState();
}

class RegistrationState extends State<Registration> {
  final TextEditingController _nameController = TextEditingController();
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _contactController = TextEditingController();
  final TextEditingController _addressController = TextEditingController();
  final TextEditingController _districtController = TextEditingController();
  final TextEditingController _placeController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

  String? selectedDistrict;
  String? selectedPlace;
  
  List<Map<String, dynamic>> districts = [];
  List<Map<String, dynamic>> places = [];

  @override
  void initState() {
    super.initState();
    fetchDistricts();
  }

  Future<void> fetchDistricts() async {
    try {
      QuerySnapshot<Map<String, dynamic>> querySnapshot =
          await FirebaseFirestore.instance.collection('tbl_district').get();

      List<Map<String, dynamic>> tempDistricts = querySnapshot.docs
          .map((doc) => {
                'id': doc.id,
                'name': doc['district_name'].toString(),
              })
          .toList();

      setState(() {
        districts = tempDistricts;
      });
    } catch (e) {
      print('Error fetching district data: $e');
    }
  }

  Future<void> fetchPlaceData(id) async {
    try {
      print(id);
      // Replace 'tbl_course' with your actual collection name
      QuerySnapshot<Map<String, dynamic>> querySnapshot1 =
          await FirebaseFirestore.instance
              .collection('tbl_place')
              .where('District_id', isEqualTo: id)
              .get();

      List<Map<String, dynamic>> place = querySnapshot1.docs
          .map((doc) => {
                'id': doc.id,
                'name': doc['Place_name'].toString(),
              })
          .toList();

      setState(() {
        places = place;
      });
      print(places);
    } catch (e) {
      print('Error fetching place data: $e');
    }
  }

  XFile? _selectedImage;
  String? _imageUrl;
  Future<void> _pickImage() async {
    final pickedFile =
        await ImagePicker().pickImage(source: ImageSource.gallery);

    if (pickedFile != null) {
      setState(() {
        _selectedImage = XFile(pickedFile.path);
      });
    }
  }

  void register() {
    print(_nameController.text);
    print(_emailController.text);
    print(_contactController.text);
    print(_addressController.text);
    print(_districtController.text);
    print(_placeController.text);
    print(_passwordController.text);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Row(
          children: [
            Icon(Icons.person), // Add an icon to the left of the title
            SizedBox(width: 8),
            Text('User Registration'),
          ],
        ),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: ListView(
          children: [
            SizedBox(
              height: 10,
            ),
            Center(
              child: Text(
                'User Registration',
                style: TextStyle(
                    fontSize: 40.0,
                    fontWeight: FontWeight.bold,
                    color: Colors.blueAccent),
              ),
            ),
            SizedBox(
              height: 20,
            ),
            Center(
              child: GestureDetector(
                onTap: _pickImage,
                child: Stack(
                  children: [
                    CircleAvatar(
                      radius: 50,
                      backgroundColor: const Color(0xff4c505b),
                      backgroundImage: _selectedImage != null
                          ? FileImage(File(_selectedImage!.path))
                          : _imageUrl != null
                              ? NetworkImage(_imageUrl!)
                              : const AssetImage('assets/pic_11.png')
                                  as ImageProvider,
                      child: _selectedImage == null && _imageUrl == null
                          ? const Icon(
                              Icons.add,
                              size: 40,
                              color: Color.fromARGB(255, 134, 134, 134),
                            )
                          : null,
                    ),
                    if (_selectedImage != null || _imageUrl != null)
                      const Positioned(
                        bottom: 0,
                        right: 0,
                        child: CircleAvatar(
                          backgroundColor: Colors.white,
                          radius: 18,
                          child: Icon(
                            Icons.edit,
                            size: 18,
                            color: Colors.black,
                          ),
                        ),
                      ),
                  ],
                ),
              ),
            ),
            SizedBox(
              height: 10,
            ),
            TextFormField(
              controller: _nameController,
              decoration: InputDecoration(
                prefixIcon: Icon(Icons.account_circle_sharp),
                labelText: 'Name',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(
              height: 10,
            ),
            TextFormField(
              controller: _emailController,
              decoration: InputDecoration(
                prefixIcon: Icon(Icons.email),
                labelText: 'Email',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(
              height: 10,
            ),
            TextFormField(
              controller: _contactController,
              decoration: InputDecoration(
                prefixIcon: Icon(Icons.phone),
                labelText: 'Contact',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(
              height: 10,
            ),
            TextFormField(
              controller: _addressController,
              decoration: InputDecoration(
                prefixIcon: Icon(Icons.home),
                labelText: 'Address',
                border: OutlineInputBorder(),
              ),
            ),
           
            SizedBox(
              height: 10,
            ),
            DropdownButtonFormField<String>(
              value: selectedDistrict,
              decoration: InputDecoration(
                prefixIcon: const Icon(Icons.school),
                hintText: 'District',
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(10.0),
                  borderSide: const BorderSide(
                    color: Colors.blue,
                  ), // Adjust color as needed
                ),
              ),
              onChanged: (String? newValue) {
                fetchPlaceData(newValue);
                setState(() {
                  selectedDistrict = newValue;
                });
              },
              isExpanded: true,
              items: districts.map<DropdownMenuItem<String>>(
                (Map<String, dynamic> district) {
                  return DropdownMenuItem<String>(
                    value: district['id'], // Use document ID as the value
                    child: Text(district['name']),
                  );
                },
              ).toList(),
            ),
            SizedBox(
              height: 10,
            ),
            DropdownButtonFormField<String>(
              decoration: InputDecoration(
                prefixIcon: Icon(Icons.location_on),
                labelText: 'Place',
                border: OutlineInputBorder(),
              ),
              onChanged: (String? newValue) {
                setState(() {
                  selectedPlace = newValue;
                });
              },
              isExpanded: true,
              items: places.map<DropdownMenuItem<String>>(
                (Map<String, dynamic> place) {
                  return DropdownMenuItem<String>(
                    value: place['id'], // Use document ID as the value
                    child: Text(place['name']),
                  );
                },
              ).toList(),
            ),
            SizedBox(
              height: 10,
            ),
            TextFormField(
              obscureText: true,
              controller: _passwordController,
              decoration: InputDecoration(
                prefixIcon: Icon(Icons.security),
                labelText: 'Password',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(
              height: 20,
            ),
            ElevatedButton(
              onPressed: () {
                register();
              },
              style: ElevatedButton.styleFrom(
                primary: Colors.blue, // background color
                onPrimary: Colors.white, // text color
                padding: EdgeInsets.symmetric(horizontal: 20, vertical: 10),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(10),
                ),
              ),
              child: Text('Register'),
            )
          ],
        ),
      ),
    );
  }
}
