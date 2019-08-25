//
//  Log.swift
//  Freetime
//
//  Created by Brandon Titus on 8/22/19.
//  Copyright © 2019 Ryan Nystrom. All rights reserved.
//

import Foundation
import os.log

struct Log {
    @available(iOS 12.0, *)
    static let pointsOfInterest = OSLog(subsystem: "io.titus.githawk", category: .pointsOfInterest)
}
