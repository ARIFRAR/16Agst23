from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from multiselectfield.db.fields import MaxValueMultiFieldValidator



class Wedding(models.Model):
    MC_choice = (
        ('MC_Akad', 'MC Akad'),
        ('MC_Resepsi', 'MC Resepsi'),
        ('-', '-'),
    )

    catering_choices = (
        ('nasi', 'Nasi'),
        ('aneka_daging_standar', 'Aneka daging standar'),
        ('aneka_ayam_ikan_standar', 'Aneka Ayam/Ikan Standar'),
        ('cah_sayuran', 'Cah Sayuran'),
        ('kerupuk', 'Kerupuk'),
        ('sop', 'Sop'),
        ('air_mineral', 'Air Mineral'),
        ('buah_potong', 'Bua Potong'),
        ('puding_fla', 'Puding Fla'),
        ('soft_drink_matcha_tea', 'Soft Drink/Matcha Tea'),
        ('stall_75_pack', 'STALL(75 pack)'),
        ('kebab_zuppa_aneka_pasta', 'Kebab/Zuppa/Aneka Pasta'),
        ('bakso_malang', 'Bakso Malang'),
        ('mie_kocok', 'Mie Kocok'),
        ('baso_tahu', 'Baso Tahu'),
        ('empal_gentong', 'Empal Gentong'),
        ('paket_catering_andromeda', 'Paket Catering Andromeda'),
        ('-','-'),
    )

    Mua_Attire_choices = (
        ('rias_akad_pengantin', 'Rias Akad Pengantin'),
        ('busana_akad_pengantin', 'Busana Akad Pengantin'),
        ('rias_busana_orang_tua', 'Rias & Busana Orang Tua'),
        ('melati_untuk_cpp', 'Melati Untuk CPP'),
        ('makeup_akad_touchup_resepsi', 'Make Up Akad & Touch Up Resepsi'),
        ('kebaya_akad_dan_resepsi', 'Kebaya Akad Dan Resepsi'),
        ('makeup_hairdo_jilbab_ibu_kedua_mempelai', 'Make Up Hairdo/Jilbab Ibu Kedua Mempelai'),
        ('dua_set_kebaya_ibu_kedua_mempelai', 'Dua Set Kebaya Ibu Kedua Mempelai'),
        ('beskap_jas_pengantin_akad_dan_resepsi', 'Beskap/Jas Pengantin Akad Dan Resepsi'),
        ('aksesoris_pengantin_akad_resepsi', 'Aksesoris Pengantin Akad & Resepsi'),
        ('dua_set_beskap_bapak_kedua_mempelai', 'Dua Set Beskap Bapak Kedua Mempelai'),
        ('kalung_melati_pengantin', 'Kalung Melati Pengantin'),
        ('soft_lens', 'Soft Lens'),
        ('hand_bouquet', 'Hand Bouquet'),
        ('-','-'),
    )

    dekorasi_choices = (
        ('backdrop_akad_5m', 'Backdrop Akad 5 Meter'),
        ('backdrop_akad_6m', 'Backdrop Akad 6 Meter'),
        ('backdrop_akad_6-8m', 'Backdrop Akad 6-8 Meter'),
        ('lighting_backdrop', 'Lighting Backdrop'),
        ('fresh_flower_3titik', 'Fresh Flower 3 Titik'),
        ('standing_flower_4buah', 'Standing Flower 4 Buah'),
        ('standing_flower_jalan_6buah', 'Standing Flower jalan 6 Buah'),
        ('pergola_3x3', 'Pergola 3×3'),
        ('backdrop_penerima_tamu', 'Backdrop Penerima Tamu'),
        ('meja_kursi_akad', 'Meja Dan Kursi Akad'),
        ('area_penerima_tamu', 'Area Penerima Tamu'),
        ('meja_kursi_penerima_tamu', 'Meja Dan Kursi Penerima Tamu'),
        ('photo_booth', 'Photo Booth'),
        ('kotak_angpau_4buah', 'Kotak Angpau 4 Buah'),
        ('dekorasi_area_catering', 'Dekorasi Area Catering'),
        ('karpet_jalan', 'Karpet Jalan'),
        ('janur_1buah', 'Janur 1 Buah'),
        ('dekorasi_area_vip_pengantin', 'Dekorasi Area VIP & Pengantin'),
        ('hand_bouquet_lempar', 'Hand Bouquet Lempar'),
        ('buku_tamu', 'Buku Tamu'),
        ('kotak_angpau_2buah', 'Kotak Angpau 2 Buah'),
        ('welcome_sign', 'Welcome Sign'),
        ('-','-'),
    )

    dokumentasi_choices = (
        ('backdrop_foto_video_akad', 'Backdrop Foto & Video Akad'),
        ('backdrop_foto_video_akad_resepsi', 'Backdrop Foto, Video Akad & Resepsi'),
        ('cetak_1_album_kolase', 'Cetak 1 Album Kolase'),
        ('cetak_1_album_magazine_style', '1 Album Magazine Style 8Rp (20×30)'),
        ('1_box_album_custom', '1 Box Album Custom'),
        ('fresh_flower_3_titik', 'Fresh Flower 3 Titik'),
        ('standing_flower_4_buah', 'Standing Flower 4 Buah'),
        ('video_liputan_cinematic', 'Video Liputan & Cinematic'),
        ('video_cinematic_wedding', 'Video Cinematic Wedding'),
        ('cetakan_perbesaran_16rp_frame', 'Cetakan Perbesaran 16Rp & Frame'),
        ('soft_copy_on_dvd', 'Soft Copy On DVD'),
        ('all_photo_dalam_dvd', 'All Photo Dalam DVD'),
        ('-','-'),
    )

    wedding_organizer_choices = (
        ('person_in_charge_2_3_orang', 'Person In Charge 2-3 Orang'),
        ('person_in_charge_4_orang', 'Person In Charge 4 Orang'),
        ('technical_meeting_all_vendors', 'Technical Meeting All Vendors'),
        ('seragam_wo_ht', 'Seragam WO & HT'),
        ('konsultasi_acara', 'Konsultasi Acara (Konsep dll)'),
        ('satu_kali_family_meeting', 'Satu Kali Family Meeting'),
        ('koordinasi_vendor', 'Koordinasi Vendor'),
        ('satu_kali_technical_meeting_seluruh_vendor', 'Satu Kali Technical Meeting Seluruh Vendor'),
        ('hand_sanitizer', 'Hand Sanitizer'),
        ('pengaturan_acara_hari_h', 'Pengaturan Acara Hari H'),
        ('handy_talky', 'Handy Talky'),
        ('person_in_charge_saat_acara_4_orang', 'Person In Charge Saat Acara 4 Orang'),
        ('seragam_wo', 'Seragam WO'),
        ('vip_service', 'VIP Service'),
        ('pembuatan_buku_panduan_acara_pernikahan', 'Pembuatan Buku Panduan Acara Pernikahan'),
        ('pembuatan_rundown_acara', 'Pembuatan Rundown Acara'),
        ('-','-'),
    )

    music_sound_choices = (
        ('musik_3_personel', 'Musik 3 Personel'),
        ('musik_4_personel', 'Musik 4 Personel'),
        ('sound_system_1000_watt', 'Sound System 1000 Watt'),
        ('sound_system_3000_watt', 'Sound System 3000 Watt'),
        ('-','-'),
    )

    Paket = models.CharField(max_length=255)
    kota = models.CharField(max_length=255)
    provinsi = models.CharField(max_length=255)
    durasi_acara = models.CharField(max_length=255)
    description = RichTextField()
    master_of_ceremony = models.CharField(choices=MC_choice, max_length=100)
    Harga = models.IntegerField()
    catering_pack = models.IntegerField()
    wedding_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    wedding_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    wedding_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    wedding_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    wedding_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    catering = MultiSelectField(choices=catering_choices)
    MUA = MultiSelectField(choices=Mua_Attire_choices)
    Dekorasi = MultiSelectField(choices=dekorasi_choices)
    dokumentasi = MultiSelectField(choices=dokumentasi_choices)
    wedding_organizer = MultiSelectField(choices=wedding_organizer_choices)
    music_sound = MultiSelectField(choices=music_sound_choices)
    Unggulan = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.Paket) 