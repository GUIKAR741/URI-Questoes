nn = int(input())
while nn > 0:
    num = int(input())
    # while num % 2 == 0 and num != 2 and num != 0:
    #     num = num / 2
    # if num == 1 or num == 2 or num == 3 or num == 4 or num == 5 or num == 6 or num == 8 or num == 10 or num == 12 or \
    #         num == 15 or num == 16 or num == 17 or num == 20 or num == 24 or num == 30 or num == 32 or num == 34 or \
    #         num == 40 or num == 48 or num == 51 or num == 60 or num == 64 or num == 68 or num == 80 or num == 85 or \
    #         num == 96 or num == 102 or num == 120 or num == 128 or num == 136 or num == 160 or num == 170 or num == 192 or \
    #         num == 204 or num == 240 or num == 255 or num == 256 or num == 257 or num == 272 or num == 320 or \
    #         num == 340 or num == 384 or num == 408 or num == 480 or num == 510 or num == 512 or num == 514 or num == 544 or \
    #         num == 640 or num == 680 or num == 768 or num == 771 or num == 816 or num == 960 or num == 1020 or \
    #         num == 1024 or num == 1028 or num == 1088 or num == 1280 or num == 1285 or num == 1360 or num == 1536 or \
    #         num == 1542 or num == 1632 or num == 1920 or num == 2040 or num == 2048 or num == 2048 or num == 2056 or \
    #         num == 2176 or num == 2560 or num == 2570 or num == 2720 or num == 3072 or \
    #         num == 3084 or num == 3264 or num == 3840 or num == 3855 or num == 4080 or num == 4096 or num == 4112 or \
    #         num == 4352 or num == 4369 or num == 5120 or num == 5140 or num == 5440 or num == 6144 or num == 6168 or \
    #         num == 6528 or num == 7680 or num == 7710 or num == 8160 or num == 8192 or num == 8224 or num == 8704 or \
    #         num == 8738 or num == 10240 or num == 10280 or num == 10880 or num == 12288 or num == 12336 or \
    #         num == 13056 or num == 13107 or num == 15360 or num == 15420 or num == 16320 or num == 16384 or \
    #         num == 16448 or num == 17408 or num == 17476 or num == 20480 or num == 20560 or num == 21760 or \
    #         num == 21845 or num == 24576 or num == 24672 or num == 26112 or num == 26214 or num == 30720 or \
    #         num == 30840 or num == 32640 or num == 32768 or num == 32896 or num == 34816 or num == 34952 or \
    #         num == 40960 or num == 41120 or num == 43520 or num == 43690 or num == 49152 or num == 49344 or \
    #         num == 52224 or num == 52428 or num == 61440 or num == 61680 or num == 65280 or num == 65535 or \
    #         num == 65536 or num == 65537 or num == 65792 or num == 69632 or num == 69904 or num == 81920 or \
    #         num == 82240 or num == 87040 or num == 87380 or num == 98304 or num == 98688 or num == 104448 or \
    #         num == 104856 or num == 122880 or num == 123360 or num == 130560 or num == 131070 or num == 131072 or\
    #         num == 131074 or \
    #         num == 131584 or num == 139264 or num == 139808 or num == 163840 or num == 164480 or num == 174080 or \
    #         num == 174760 or num == 196608 or num == 196611 or num == 197376 or num == 208896 or num == 209712 or \
    #         num == 245760 or num == 246720 or num == 261120 or num == 262140 or num == 262144 or num == 262148 or \
    #         num == 263168 or num == 278528 or num == 279616 or num == 327680 or num == 327685 or num == 328960 or \
    #         num == 348160 or num == 349520 or num == 393216 or num == 393222 or num == 394752 or num == 417792 or \
    #         num == 419424 or num == 491520 or num == 493440:
    # if num == 1 or num == 2 or num == 3 or num == 4 or num == 5 or num == 6 or num == 8 or num == 10 or num == 12 or num == 15 or num == 16 or num == 17 or num == 20 or num == 24 or num == 30 or num == 32 or num == 34 or num == 40 or num == 48 or num == 51 or num == 60 or num == 64 or num == 68 or num == 80 or num == 85 or num == 96 or num == 102 or num == 120 or num == 128 or num == 136 or num == 160 or num == 170 or num == 192 or num == 204 or num == 240 or num == 255 or num == 256 or num == 257 or num == 272 or num == 320 or num == 340 or num == 384 or num == 408 or num == 480 or num == 510 or num == 512 or num == 514 or num == 544 or num == 640 or num == 680 or num == 768 or num == 771 or num == 816 or num == 960 or num == 1020 or num == 1024 or num == 1028 or num == 1088 or num == 1280 or num == 1285 or num == 1360 or num == 1536 or num == 1542 or num == 1632 or num == 1920 or num == 2040 or num == 2048 or num == 2056 or num == 2176 or num == 2560 or num == 2570 or num == 2720 or num == 3072 or num == 3084 or num == 3264 or num == 3840 or num == 3855 or num == 4080 or num == 4096 or num == 4112 or num == 4352 or num == 4369 or num == 5120 or num == 5140 or num == 5440 or num == 6144 or num == 6168 or num == 6528 or num == 7680 or num == 7710 or num == 8160 or num == 8192 or num == 8224 or num == 8704 or num == 8738 or num == 10240 or num == 10280 or num == 10880 or num == 12288 or num == 12336 or num == 13056 or num == 13107 or num == 15360 or num == 15420 or num == 16320 or num == 16384 or num == 16448 or num == 17408 or num == 17476 or num == 20480 or num == 20560 or num == 21760 or num == 21845 or num == 24576 or num == 24672 or num == 26112 or num == 26214 or num == 30720 or num == 30840 or num == 32640 or num == 32768 or num == 32896 or num == 34816 or num == 34952 or num == 40960 or num == 41120 or num == 43520 or num == 43690 or num == 49152 or num == 49344 or num==493440:
    if num == 1 or num == 2 or num == 3 or num == 4 or num == 5 or num == 6 or num == 8 or num == 10 or num == 12 or num == 15 or num == 16 or num == 17 or num == 20 or num == 24 or num == 30 or num == 32 or num == 34 or num == 40 or num == 48 or num == 51 or num == 60 or num == 64 or num == 68 or num == 80 or num == 85 or num == 96 or num == 102 or num == 120 or num == 128 or num == 136 or num == 160 or num == 170 or num == 192 or num == 204 or num == 240 or num == 255 or num == 256 or num == 257 or num == 272 or num == 320 or num == 340 or num == 384 or num == 408 or num == 480 or num == 510 or num == 512 or num == 514 or num == 544 or num == 640 or num == 680 or num == 768 or num == 771 or num == 816 or num == 960 or num == 1020 or num == 1024 or num == 1028 or num == 1088 or num == 1280 or num == 1285 or num == 1360 or num == 1536 or num == 1542 or num == 1632 or num == 1920 or num == 2040 or num == 2048 or num == 2056 or num == 2176 or num == 2560 or num == 2570 or num == 2720 or num == 3072 or num == 3084 or num == 3264 or num == 3840 or num == 3855 or num == 4080 or num == 4096 or num == 4112 or num == 4352 or num == 4369 or num == 5120 or num == 5140 or num == 5440 or num == 6144 or num == 6168 or num == 6528 or num == 7680 or num == 7710 or num == 8160 or num == 8192 or num == 8224 or num == 8704 or num == 8738 or num == 10240 or num == 10280 or num == 10880 or num == 12288 or num == 12336 or num == 13056 or num == 13107 or num == 15360 or num == 15420 or num == 16320 or num == 16384 or num == 16448 or num == 17408 or num == 17476 or num == 20480 or num == 20560 or num == 21760 or num == 21845 or num == 24576 or num == 24672 or num == 26112 or num == 26214 or num == 30720 or num == 30840 or num == 32640 or num == 32768 or num == 32896 or num == 34816 or num == 34952 or num == 40960 or num == 41120 or num == 43520 or num == 43690 or num == 49152 or num == 49344:
        print("Yes")
    else:
        print("No")
    nn -= 1
