$directory = '/tmp/sajjad';
opendir (DIR,$directory) or die $!;
while($file = readdir(DIR)){
    next if ($file =~m/^\./);
    print "$file\n";
}
closedir(DIR);
exit 0;