#include <stdio.h>

int main( void )
{
// 用户定义
char plain_text[128];
const size_t cipher = 3;

// 辅助变量
char cipher_text[ sizeof(plain_text)/sizeof(*plain_text) ];
const size_t maxlen = sizeof(plain_text)/sizeof(*plain_text);
size_t len = 0;

// 输入（以回车结束）
printf( "%s", "Input a text please: " );
for( int ch; len!=maxlen-1 && (ch=getchar(), ch!=EOF && ch!='\n'); )
{
if( ch>='A' && ch<='Z' )
plain_text[len++] = (char)ch;
else if( ch>='a' && ch<='z' )
plain_text[len++] = (char)ch-('a'-'A');
}
plain_text[len] = '\0';
cipher_text[len] = '\0';
printf( "plain text: %s\n", plain_text );

// 加密
for( size_t i=0; i!=len; ++i )
cipher_text[i] = (plain_text[i]-'A'+cipher%26)%26 + 'A';
printf( "cipher text: %s\n", cipher_text );

// 解密
for( size_t i=0; i!=len; ++i )
cipher_text[i] = (cipher_text[i]-'A'+26-cipher%26)%26 + 'A';
printf( "decipher text: %s\n", cipher_text );
} 
