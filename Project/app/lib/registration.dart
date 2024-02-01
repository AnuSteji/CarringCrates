import 'dart:io';
import 'package:carring_crates/login.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_storage/firebase_storage.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:image_picker/image_picker.dart';
import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:file_picker/file_picker.dart';
import 'package:progress_dialog_null_safe/progress_dialog_null_safe.dart';

class Registration extends StatefulWidget {
  const Registration({Key? key}) : super(key: key);

  @override
  State<Registration> createState() => RegistrationState();
}

class RegistrationState extends State<Registration> {
  final TextEditingController _nameController = TextEditingController();
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _contactController = TextEditingController();
  final TextEditingController _addressController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  XFile? _selectedImage;
  String? _imageUrl;
  String? filePath;
  late ProgressDialog _progressDialog;
  @override
  void initState() {
    super.initState();
    _progressDialog = ProgressDialog(context);
    fetchDistricts();
  }

  String? selectedDistrict;
  String? selectedPlace;

  List<Map<String, dynamic>> districts = [];
  List<Map<String, dynamic>> places = [];

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
    places = [];
    try {
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
    } catch (e) {
      print('Error fetching place data: $e');
    }
  }

  Future<void> _pickFile() async {
    try {
      FilePickerResult? result = await FilePicker.platform.pickFiles();

      if (result != null) {
        setState(() {
          filePath = result.files.single.path;
        });
      } else {
        // User canceled file picking
        print('File picking canceled.');
      }
    } catch (e) {
      // Handle exceptions
      print('Error picking file: $e');
    }
  }

  Future<void> _pickImage() async {
    final pickedFile =
        await ImagePicker().pickImage(source: ImageSource.gallery);

    if (pickedFile != null) {
      setState(() {
        _selectedImage = XFile(pickedFile.path);
      });
    }
  }

  Future<void> register() async {
    try {
      _progressDialog.show();
      UserCredential userCredential =
          await FirebaseAuth.instance.createUserWithEmailAndPassword(
        email: _emailController.text,
        password: _passwordController.text,
      );

      if (userCredential != null) {
        await _storeUserData(userCredential.user!.uid);
        Fluttertoast.showToast(
          msg: "Registration Successful",
          toastLength: Toast.LENGTH_SHORT,
          gravity: ToastGravity.BOTTOM,
          backgroundColor: Colors.green,
          textColor: Colors.white,
        );
        _progressDialog.hide();
        Navigator.pushReplacement(
          context,
          MaterialPageRoute(builder: (context) => Login()),
        );
      }
    } catch (e) {
      _progressDialog.hide();
      Fluttertoast.showToast(
        msg: "Registration Failed",
        toastLength: Toast.LENGTH_SHORT,
        gravity: ToastGravity.BOTTOM,
        backgroundColor: Colors.red,
        textColor: Colors.white,
      );
      print("Error registering user: $e");
      // Handle error, show message, or take appropriate action
    }
  }

  Future<void> _storeUserData(String userId) async {
    try {
      final FirebaseFirestore firestore = FirebaseFirestore.instance;
      await firestore.collection('tbl_userregistration').doc(userId).set({
        'user_name': _nameController.text,
        'user_email': _emailController.text,
        'user_contact': _contactController.text,
        'user_address': _addressController.text,
        'user_password': _passwordController.text,
        'User_id': userId,
      });

      await _uploadImage(userId);
    } catch (e) {
      print("Error storing user data: $e");
      // Handle error, show message or take appropriate action
    }
  }

  Future<void> _uploadImage(String userId) async {
    try {
      if (_selectedImage != null) {
        Reference ref =
            FirebaseStorage.instance.ref().child('User_photo/$userId.jpg');
        UploadTask uploadTask = ref.putFile(File(_selectedImage!.path));
        TaskSnapshot taskSnapshot = await uploadTask.whenComplete(() => null);

        String imageUrl = await taskSnapshot.ref.getDownloadURL();

        await FirebaseFirestore.instance
            .collection('tbl_userregistration')
            .doc(userId)
            .update({
          'user_photo': imageUrl,
        });
      }

      if (filePath != null) {
        //FileUpload
        // Step 1: Get the file name from the path
        String fileName = filePath!.split('/').last;

        // Step 2: Upload file to Firebase Storage with the original file name
        Reference fileRef = FirebaseStorage.instance
            .ref()
            .child('User_proof/$userId/$fileName');
        UploadTask fileUploadTask = fileRef.putFile(File(filePath!));
        TaskSnapshot fileTaskSnapshot =
            await fileUploadTask.whenComplete(() => null);

        // Step 3: Get download URL of the uploaded file
        String fileUrl = await fileTaskSnapshot.ref.getDownloadURL();

        // Step 4: Update user's collection in Firestore with the file URL
        await FirebaseFirestore.instance
            .collection('tbl_userregistration')
            .doc(userId)
            .update({
          'user_proof': fileUrl,
        });
      }
    } catch (e) {
      print("Error uploading image: $e");
      // Handle error, show message or take appropriate action
    }
  }

  String? selectedGender;

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
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const SizedBox(
                height: 10,
              ),
              const Center(
                child: Text(
                  'User Registration',
                  style: TextStyle(
                      fontSize: 40.0,
                      fontWeight: FontWeight.bold,
                      color: Colors.blueAccent),
                ),
              ),
              const SizedBox(height: 20),
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
                                color: Color.fromARGB(255, 41, 39, 39),
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
              const SizedBox(height: 25),
              _buildIconTextField(Icons.person, _nameController, 'Name'),
              const SizedBox(height: 10),
              _buildIconTextField(Icons.email, _emailController, 'Email'),
              const SizedBox(height: 10),
              _buildIconTextField(Icons.phone, _contactController, 'Contact'),
              const SizedBox(height: 10),
              _buildIconTextField(Icons.home, _addressController, 'Address',
                  multiline: true),
              const SizedBox(height: 10),
               DropdownButtonFormField<String>(
              value: selectedDistrict,
              decoration: InputDecoration(
                prefixIcon: const Icon(Icons.location_on),
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
              const SizedBox(height: 10),
              DropdownButtonFormField<String>(
              decoration: const InputDecoration(
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
              const SizedBox(height: 10),
              Column(
                children: [
                  Row(
                    children: [
                      Expanded(
                        child: ElevatedButton(
                          onPressed: _pickFile,
                          child: Text('Choose Proof'),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(height: 16),
                  if (filePath != null)
                    Text(
                      'Selected File: $filePath',
                      style: TextStyle(fontSize: 16),
                    ),
                ],
              ),
              const SizedBox(height: 10),
              _buildIconTextField(
                  Icons.security, _passwordController, 'Password',
                  obscureText: true),
              const SizedBox(height: 30),
              ElevatedButton(
                onPressed: register,
                child: const Text('Register'),
                style: ElevatedButton.styleFrom(
                  primary: Colors.deepPurple, // Button color
                  onPrimary: Colors.white, // Text color
                  shape: RoundedRectangleBorder(
                    borderRadius:
                        BorderRadius.circular(10.0), // Rounded corners
                  ),
                  padding: const EdgeInsets.symmetric(
                      vertical: 16.0), // Set vertical padding
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildIconTextField(
      IconData icon, TextEditingController controller, String labelText,
      {bool obscureText = false, bool multiline = false}) {
    return TextFormField(
      maxLines: multiline ? null : 1,
      keyboardType: multiline ? TextInputType.multiline : TextInputType.text,
      controller: controller,
      obscureText: obscureText,
      decoration: InputDecoration(
        labelText: labelText,
        prefixIcon: Icon(icon),
        border: const OutlineInputBorder(),
      ),
    );
  }

  Widget _buildIconDropdownField(IconData icon, String? value, String hintText,
      List<String> items, void Function(String?) onChanged) {
    return DropdownButtonFormField<String>(
      value: value,
      decoration: InputDecoration(
        hintText: hintText,
        prefixIcon: Icon(icon),
        border: const OutlineInputBorder(),
      ),
      onChanged: onChanged,
      items: items.map<DropdownMenuItem<String>>((String item) {
        return DropdownMenuItem<String>(
          value: item,
          child: Text(item),
        );
      }).toList(),
    );
  }
}

