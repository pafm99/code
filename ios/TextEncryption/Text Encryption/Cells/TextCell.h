//
//  TextCell.h
//  Text Encryption
//
//  Created by Grzegorz Wójcik on 06.05.2015.
//  Copyright (c) 2015 Grzegorz Wójcik. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface TextCell : UITableViewCell <UITextViewDelegate>
@property (weak) IBOutlet UITextView *textView;
@end
