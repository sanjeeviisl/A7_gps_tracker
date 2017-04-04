#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

char t_buffer11[10];
char t_buffer22[10];
char t_buffer33[10];
char t_buffer44[10];
char send_string[ 1024 ];
char A7_device_id_str[1024];
char *dtostrf (double val, signed char width, unsigned char prec, char *sout) { 
   char fmt[20]; 
   sprintf(fmt, "%%%d.%df", width, prec); 
   sprintf(sout, fmt, val); 
   return sout; 
} 

void Resetbufer(unsigned char *buf,int size)
{
        int i;
        for(i=0;i<size;i++)
        {
                buf[i] = '0';
        }
}


int main()
{

	char * A7_latitude_str;
	char * A7_longitude_str;
	char * A7_speed_str;
	char * A7_bearing_str;

char  A7_gps_data_str[6];
char  A7_device_status_str[6];
char  A7_engine_status_str[6];
char  A7_vehicle_status_str[6];
char  A7_updated_time_str[12];
char  A7_updated_date_str[12];
	

char tcp_string1[]= "at+cipstatus\r\n";
char tcp_string2[]= "AT+CIPSTART=\"TCP\",\"www.iisl.co.in\",80\r\n";
char tcp_string3[]= "at+cipstatus\r\n";
char tcp_string4[]= "AT+CIPSEND\r\n";	

char tcp_header_str[] = "GET http://iisl.co.in/gps_control_panel/gps_mapview/addvehiclelocation.php?";	

char tcp_body_str[] = " HTTP/1.0\r\n";

char tcp_footer_str[] = "Host: www.iisl.co.in:8080\r\n";


char end_of_file_byte = (char)26;

char tcp_string_end[1];
char tcp_string_end1[]= "\r\n";

char tcp_string20[]= "AT+CIPCLOSE\r\n";
char tcp_string21[]= "at+cifsr\r\n";
tcp_string_end[0] = end_of_file_byte;

strcpy(A7_device_id_str,"1234567890");

	A7_longitude_str=dtostrf(68.00088,0,6,t_buffer11);
	A7_latitude_str=dtostrf(29.44550,0,6,t_buffer22);	
	A7_speed_str=dtostrf(30.2,0,6,t_buffer33);
	A7_bearing_str=dtostrf(180.0000000,0,6,t_buffer44);
	strcpy(A7_updated_date_str,"25-10-17");
	strcpy(A7_updated_time_str,"10-10-12");
	
	strcpy(A7_gps_data_str,"OFF");
	strcpy(A7_device_status_str,"ON");
	strcpy(A7_engine_status_str,"ON");
	strcpy(A7_vehicle_status_str,"READY");



				snprintf(send_string,sizeof(send_string),"%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s", tcp_header_str,"device_id=",A7_device_id_str,\
				"&latitude=",A7_latitude_str,"&longitude=",A7_longitude_str,"&utcdate_stamp=",A7_updated_date_str,"&utctime_stamp=",A7_updated_time_str,\
				"&speed=",A7_speed_str,"&direction=",A7_bearing_str,"&gps_data=",A7_gps_data_str,"&device_status=",A7_device_status_str,\
				"&engine_status=",A7_engine_status_str,"&vehicle_status=",A7_vehicle_status_str,tcp_body_str);

printf("send string |%s|", send_string);



}
