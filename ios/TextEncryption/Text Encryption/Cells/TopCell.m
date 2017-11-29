//
//  TopCell.m
//  Text Encryption
//
//  Created by Grzegorz Wójcik on 06.05.2015.
//  Copyright (c) 2015 Grzegorz Wójcik. All rights reserved.
//

#import "TopCell.h"

@implementation TopCell

- (void)awakeFromNib {
    [_cpyBtn setTitle:NSLocalizedString(@"Copy\nas link", nil) forState:UIControlStateNormal];
    
    [_clearBtn setTitle:NSLocalizedString(@"Clear", nil) forState:UIControlStateNormal];
    [_sendBtn setTitle:NSLocalizedString(@"Send", nil) forState:UIControlStateNormal];
}

- (void)setSelected:(BOOL)selected animated:(BOOL)animated {
    [super setSelected:selected animated:animated];

    // Configure the view for the selected state
}

@end
