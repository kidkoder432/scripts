import bs4, requests
RAGA_LIST = '''Abhogi Kanada 	Adana 	Aheer Bhairav 	Alhaiya Bilawal
Bageshree 	Bahar 	Bairagi 	Bairagi Todi
Basant 	Basant Mukhari 	Bhairav 	Bhairavi
Bhatiyar 	Bheem 	Bheempalasi 	Bhoopali
Bhupal Todi 	Bihag 	Bilaskhani Todi 	Chandrakauns
Charukeshi 	Chhayanut 	Darbari Kanada 	Des
Deshkar 	Desi 	Dev Gandhar 	Devgiri Bilawal
Devshree 	Durga 	Gaud Malhar 	Gaud Sarang
Gauri (Bhairav Ang) 	Gopika Basant 	Gorakh Kalyan 	Gunkali
Gurjari Todi 	Hameer 	Hansadhwani 	Hans Kinkini
Harikauns 	Hemant 	Hemshri 	Hindol
Jaijaivanti 	Jaldhar Kedar 	Jaunpuri 	Jayat
Jhinjhoti 	Jog 	Jogeshwari 	Pancham Jogeshwari
Jogiya 	Jogkauns 	Kafi 	Kalawati
Kamod 	Kaushik Dhwani 	Kausi Kanada 	Kedar
Keerwani 	Khamaj 	Khambavati 	Komal Rishabh Asawari
Lalit 	Lanka Dahan Sarang 	Madhukauns 	Madhumad Sarang
Madhuvanti 	Malgunji 	Malhar 	Malkauns
Mand 	Maru Bihag 	Marwa 	Megh Malhar
Mohankauns 	Multani 	Nand 	Narayani
Nayaki Kanada 	Nut-Bhairav 	Parameshwari 	Patdeep
Pilu 	Puriya 	Puriya Dhanashri 	Puriya Kalyan
Poorvi 	Rageshree 	Ramdasi Malhar 	Ramkali
Saalag Varali 	Sarang (Brindavani Sarang) 	Saraswati 	Saraswati Kedar
Shahana Kanada 	Shankara 	Shivranjani 	Shobhawari
Shree 	Shuddha Kalyan 	Shuddha Sarang 	Shyam Kalyan
Sindhura 	Sohani 	Suha Sughrai 	Sundarkali
Sundarkauns 	Surdasi Malhar 	Tilak Kamod 	Tilang
Tilang Bahar 	Todi 	Vachaspati 	Vibhas
Yaman'''.split('  ')
print(RAGA_LIST)