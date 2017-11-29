//
//  TopCell.m
//  Text Encryption
//
//  Created by Grzegorz Wójcik on 06.05.2015.
//  Copyright (c) 2015 Grzegorz Wójcik. All rights reserved.
//

#import "BottomCell.h"

@implementation BottomCell

- (void)awakeFromNib {
    [_encryptBtn setTitle:NSLocalizedString(@"Encrypt", nil) forState:UIControlStateNormal];
    [_decryptBtn setTitle:NSLocalizedString(@"Decrypt", nil) forState:UIControlStateNormal];
}

- (void)setSelected:(BOOL)selected animated:(BOOL)animated {
    [super setSelected:selected animated:animated];

    // Configure the view for the selected state
}

@end
